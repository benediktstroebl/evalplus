Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Only returns the first solution, even if there are multiple zeros.
    Guarantees a solution only for lists of coefficients with an even count
    and the largest coefficient not equal to zero.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # Calculates discriminant of corresponding quadratic equation
    discriminant = (sum(coefficients[1:]) * len(coefficients) + sum(coefficients[1:])**2 / 4) / (len(coefficients) - 2)

    # Returns solution of quadratic equation for x
    return (-discriminant + math.sqrt(discriminant**2 - 4 * sum(coefficients[1:]) / (len(coefficients) - 2))) / 2
```

This script defines the `poly` and `find_zero` functions as specified in the prompt. You can use the `poly` function to evaluate the polynomial at a given point, and the `find_zero` function to find a solution for the polynomial equation `poly(x) = 0`.

The `find_zero` function handles some edge cases where it cannot guarantee a solution or where there may not be a solution. It returns `None` in these cases. 

Keep in mind that the function can only guarantee a solution for a polynomial with an even count of coefficients and a largest non-zero coefficient. 

Please note that the function assumes that the list of coefficients is valid and does not perform validation. It assumes the input is a list of numbers, even if the prompt doesn't explicitly state this. If you have any other constraints or requirements for the input, you may need to add additional checks or validation steps.