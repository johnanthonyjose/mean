from mypkg.mod import fibonacci, sinc2d, c
import numpy as np

def test_fibonacci0():
    # test edge 0
    obs = fibonacci(0)
    assert obs == 1

def test_fibonacci1():
    # test edge 1
    obs = fibonacci(1)
    assert obs == 1

def test_fibonacci6():
    # test internal point
    obs = fibonacci(6)
    assert obs == 8

def test_internal():
    exp = (2.0 / np.pi) * (-2.0 / (3.0 * np.pi))
    obs = sinc2d(np.pi / 2.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_x():
    exp = (-2.0 / (3.0 * np.pi))
    obs = sinc2d(0.0, 3.0 * np.pi / 2.0)
    assert obs == exp

def test_edge_y():
    exp = (2.0 / np.pi)
    obs = sinc2d(np.pi / 2.0, 0.0)
    assert obs == exp

def test_edge_xy():
    exp = 1
    obs = sinc2d(0.0, 0.0)
    assert obs == exp
"""
Integration Tests
You can think of a software project like a clock. Functions and classes are the gears and cogs that make up the system. On their own, they can be of the highest quality. Unit tests verify that each gear is well made. However, the clock still needs to be put together. The gears need to fit with one another.
Because they deal with gluing code together, there are typically fewer integration tests in a test suite than there are unit tests. However, integration tests are no less important. Integration tests are essential for having adequate testing. They encompass all of the cases that you cannot hit through plain unit testing.

Sometimes, especially in probabilistic or stochastic codes, the precise behavior of an integration test cannot be determined beforehand. That is OK. In these situations it is acceptable for integration tests to verify average or aggregate behavior rather than exact values. Sometimes you can mitigate nondeterminism by saving seed values to a random number generator, but this is not always going to be possible. It is better to have an imperfect integration test than no integration test at all.

As a simple example, consider the three functions a(), b(), and c(). The a() function adds one to a number, b() multiplies a number by two, and c() composes them. These functions are defined as follows:
"""
def test_c():
    exp = 6
    obs = c(2)
    assert obs == exp