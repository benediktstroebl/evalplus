Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of terms: coefficients[0] + coefficients[1] * x + coefficients[2] * x^2 + ... + coefficients[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])

def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation: poly(x) = 0.
    Returns only one solution, even if there are many.
    Works only for lists with even numbers of coefficients, and with the largest non-zero coefficient.
    """
    if len(coefficients) % 2 == 1:
        raise ValueError("List of coefficients must have an even number of elements")
    if coefficients[-1] == 0:
        raise ValueError("List of coefficients must have a largest non-zero coefficient")

    # Divide coefficients into pairs of equal coefficients
    # i.e [a1, a2, a3, a4] => [([a1, a2], [a3, a4])
    pairs = zip(coefficients[:len(coefficients) // 2], coefficients[len(coefficients) // 2:])
    # Find angles for which tangent is equal to zero
    for pair in pairs:
        x_minus = poly(pair, -1) / poly(pair, +1)
        if abs(x_minus) < 1e-6:
            return math.sqrt(-x_minus)
    else:
        raise ValueError("Unable to find solution")
```

This script includes two functions. The `poly` function evaluates a polynomial with a given list of coefficients at a given point `x`. The `find_zero` function takes a list of coefficients and finds a solution for the equation `poly(x) = 0`. It only returns one solution, even if there are multiple, and only works with lists that have an even number of coefficients and a largest non-zero coefficient. 

The `find_zero` function divides the coefficients into pairs and loops through each pair of even and odd coefficients. It then calculates `x_minus`, the evaluation of the polynomial at x-1, and `x_plus`, the evaluation of the polynomial at x+1. If `x_minus` is close to zero, it returns the square root of `x_minus`. 

The script also includes test cases to ensure the functions are correct:
```python
# Tests
assert round(find_zero([1, 2]), 2) == -0.5, "Test 1 failed!"

assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0, "Test 2 failed!"

assert find_zero([1, 1, 1, 1, 1]) == None, "Test 3 failed!"

assert find_zero([10, -20, 30, -40, 50]) == None, "Test 4 failed!"
``` 
Ensure you run the tests before uploading them to code form to guarantee that the answers are appropriate. You can add these tests to a separate module or script to validate the correctness of the solution.