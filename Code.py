# Portfolio Optimization Project
# Author: Moses BALUME

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Simulated returns for 3 assets
returns = np.array([0.12, 0.18, 0.15])
risk = np.array([0.10, 0.20, 0.15])  # standard deviation

# Objective function: minimize portfolio variance
def portfolio_variance(weights):
    return np.dot(weights**2, risk**2)

# Constraint: sum of weights = 1
constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

# Bounds: each weight between 0 and 1
bounds = tuple((0, 1) for _ in range(3))

# Initial guess
initial_weights = [1/3, 1/3, 1/3]

# Optimization
result = minimize(portfolio_variance, initial_weights,
                  bounds=bounds, constraints=constraints)

optimal_weights = result.x

print("Optimal Weights:", optimal_weights)
print("Expected Portfolio Return:", np.dot(optimal_weights, returns))

# Visualization
plt.bar(['Asset A','Asset B','Asset C'], optimal_weights)
plt.title("Optimal Portfolio Allocation")
plt.ylabel("Weight")
plt.show()
