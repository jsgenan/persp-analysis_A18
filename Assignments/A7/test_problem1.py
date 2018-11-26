import pytest

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1:
        return 1
    for i in range(2, int(n**.5)):
    #should be range(2, int(n**.5)+1)s
        if n % i == 0:
            return i
    return n

def test_one():
    assert smallest_factor(1)==1
def test_two():
    assert smallest_factor(4)==2
def test_three():
    assert smallest_factor(6)==2
def test_four():
    assert smallest_factor(99)==3