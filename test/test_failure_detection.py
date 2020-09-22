import pytest

def test_failure_display():
    assert 1 == 2, "This assertion should fail"

def test_second_failure_display():
    assert 5 == 17, "This assertion should fail"
