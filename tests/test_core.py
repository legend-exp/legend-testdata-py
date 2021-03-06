import pytest
from git import GitCommandError

from legend_testdata import LegendTestData

ldata = LegendTestData()
ldata.checkout('49c7bdc')


def test_get_file():
    assert (
        ldata.get_path('fcio/th228.fcio') == '/tmp/legend-testdata/data/fcio/th228.fcio'
    )


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        ldata.get_path('non-existing-file.ext')


def test_git_ref_not_found():
    with pytest.raises(GitCommandError):
        ldata.checkout('non-existent-ref')
