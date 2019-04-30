import numpy.testing as nt

from estimator import *


def test_shock_first_moments():
    n = 5000000
    X, Z, Y = fake_data(n)
    truth = np.array([0.5, 0.1, 0.1])
    s1 = get_shock_first_moments(X, Z, Y, 1)
    s2 = get_shock_first_moments(X, Z, Y, 2)
    nt.assert_array_almost_equal(s1, truth, decimal=2)
    nt.assert_array_almost_equal(s2, truth, decimal=2)


def test_shock_second_moments():
    n = 50000000
    truth = np.array([2, 0.2, 0.2, 0.05, 0.05, 0.05])
    X, Z, Y = fake_data(n)
    m1 = get_shock_first_moments(X, Z, Y, 1)
    m2 = get_shock_second_moments(X, Z, Y, 1)
    est = center_shock_second_moments(m1, m2)
    nt.assert_allclose(est, truth, atol=0, rtol=0.20)
