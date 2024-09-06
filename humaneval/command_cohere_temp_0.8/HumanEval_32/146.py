Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients * x^i = 0.
    Returns only one solution, even in case of multiple zeros.
    Works only for lists with even number of coefficients,
    and assumes the list contains the coefficient with the largest absolute value.
    """
    # your code here :)

    # check preconditions
    if len(coefficients) % 2 == 1:
        raise ValueError("list of coefficients must have even length")

    # you can assume coefficients contains max_abs_coefficient
    max_abs_coefficient = max(coefficients, key=abs)

    # we construct a matrix with 3 columns:
    # 1) coefficients relative to max_abs_coefficient
    # 2) coefficients scaled with max_abs_coefficient
    # 3) column of zeros
    coefficients_scaled = [coeff / max_abs_coefficient**i for i, coeff in enumerate(coefficients)]
    coefficients_scaled.extend([0] * (len(coefficients) - len(coefficients_scaled)))

    # construct matrix
    A = [[coefficients_scaled[i * 2 + j] for j in range(len(coefficients_scaled) // 2)]
                for i in range(len(coefficients_scaled) // 2)]

    # fetch inverse
    try:
        invA = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        raise ValueError("polynomial does not have a zero")

    # inverse is a 2x2 matrix, so we grab x from there
    return invA[0, 0] + invA[1, 0] * 1.0
```

The code assumes that Numpy is installed, and that the list of coefficients is either scaled (largest coefficient is 1),
or that the largest coefficient is removed and a coefficient scaling factor is provided.
The latter is done using the max_abs_coefficient parameter as used in the find_zero method.

Please let me know if this solution suits your needs or if you have any further questions!