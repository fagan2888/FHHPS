import logging
from time import time

from fhhps.estimator import FHHPSEstimator
from fhhps.utils import generate_data

logging.basicConfig(level=logging.INFO)

# Simulation config
n = 2000000
fake = generate_data(n=n)
data = fake["df"]

# Algorithm configuration
est = FHHPSEstimator(shock_const=5.0,
                     shock_alpha=0.2,
                     coef_const=10.,
                     coef_alpha=0.1,
                     censor1_const=1.0,
                     censor2_const=1.0)
est.add_data(X=data[["X1", "X2", "X3"]],
             Z=data[["Z1", "Z2", "Z3"]],
             Y=data[["Y1", "Y2", "Y3"]])

# Computing all objects
t1 = time()
est.fit_shock_means()
est.fit_shock_second_moments()

# est.fit_output_cond_means()
# est.fit_coefficient_means()
# est.fit_output_cond_means()
# est.fit_coefficient_means()
# est.fit_output_cond_cov()
# est.fit_coefficient_second_moments()
t2 = time()
print(f"Fiitting took {t2 - t1} seconds")

print("SHOCKS")
print("Means:")
print(est.shock_means)
print("Covariances:")
print(est.shock_cov)

print("RANDOM COEFFICIENTS")
print("Means:")
print(est.coefficient_means)
print("Covariances:")
print(est.coefficient_cov)
