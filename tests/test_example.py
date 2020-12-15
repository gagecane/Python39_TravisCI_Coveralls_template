from mypkg import app
import pytest

def test_passes():
    assert app.alwaysTrue() == True