```python
import math
def find_polynomial_root(xs):
    """
    Find the roots of a polynomial using rationalization
    """
    # Ensure valid input
    assert len(xs) == 2
    assert all(xs[0] >= 0 and xs[1] >= 0)
    assert xs[0] + xs[1] > 0

    # Perform rationalization and get roots
    numerator = xs[0] * xs[1]
    denominator = xs[0] + xs[1]
    x_root1, x_root2 = math.sqrt(numerator / denominator)
    return x_root1, x_root2

def test_find_polynomial_root():
    """
    Test the find_polynomial_root function
    """
    # Example polynomial coefficients
    xs = [1, 2]

    # Call the function and check the output
    root1, root2 = find_polynomial_root(xs)
    assert root1 == root2
    assert root1 >= 0
    assert root2 >= 0

if __name__ == "__main__":
    # Test the function
    test_find_polynomial_root()
```
The function `find_polynomial_root` in this script uses rationalization to find the roots of a polynomial. It accepts two coefficients as input and returns the two roots. The test function `test_find_polynomial_root` contains an example polynomial coefficients list and passes it to the `find_polynomial_root` function to test the function.