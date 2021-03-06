import os
import os.path as path

from git import InvalidGitRepositoryError, Repo


class LegendTestData:
    def __init__(self):
        self._default_git_ref = 'main'
        self._repo_path = '/tmp/legend-testdata'
        self._repo: Repo = self._init_testdata_repo()

    def _init_testdata_repo(self):

        if not path.isdir(self._repo_path):
            os.mkdir(self._repo_path)

        repo = None
        try:
            repo = Repo(self._repo_path)
        except InvalidGitRepositoryError:
            repo = Repo.clone_from(
                'https://github.com/legend-exp/legend-testdata', self._repo_path
            )

        repo.git.checkout(self._default_git_ref)

        return repo

    def checkout(self, git_ref: str):
        self._repo.git.checkout(git_ref)

    def reset(self):
        self._repo.git.checkout(self._default_git_ref)

    def get_path(self, filename: str):
        """Get an absolute path to a LEGEND test data file

        Parameters
        ----------
        filename : str
            path of the file relative to legend-testdata/data
        """

        full_path = path.abspath(path.join(self._repo_path, 'data', filename))

        if not path.isfile(full_path):
            raise FileNotFoundError(
                f'Test file "{filename}" not found in legend-testdata repository'
            )

        return full_path
