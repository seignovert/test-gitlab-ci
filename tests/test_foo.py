import pytest

from foo import foo

def test_foo():
    assert foo() == 'foo'