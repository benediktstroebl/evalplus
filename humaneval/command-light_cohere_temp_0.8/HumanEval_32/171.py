```python
import math

def find_poly_root(xs: list):
    """
    Given a list of coefficients xs, finds the polynomial root.
    Parameters:
        xs (list): list of coefficients of the polynomial

    Returns:
        float: root of the polynomial
    """
    n = len(xs)
    if n == 0:
        return None
    elif n == 1:
        return xs[0]
    else:
        m = n // 2
        xl = [xs[i] for i in range(m)]
        yl = [xs[i] * x[i] for i in range(m)]
        return roots.poly(yl)

def test_find_poly_root():
    """
    Unit tests for the find_poly_root function.

    Returns: number of test cases passed.
    """
    test_cases = [[1, 1], [2, -4], [5, 5]]
    """
    assert len(find_poly_root(test_cases)) == 3

if __name__ == "__main__":
    test_cases = [[1, 1], [2, -4], [5, 5]]
    find_poly_root(test_cases)
```
The Python script defines two functions: 'find_poly_root' and 'test_find_poly_root'. 'find_poly_root' finds the root of a polynomial, while 'test_find_poly_root' tests the 'find_poly_root' function with some unit test cases.