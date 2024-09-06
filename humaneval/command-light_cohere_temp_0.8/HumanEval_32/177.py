```python
import math

def find_zero(xs):
    """
    Find zeros of the polynomial represented by xs.
    if len(xs) != even:
        return "Error: list of coefficients must have even length."
    # Sort coefficients to make the algorithm faster
    xs.sort()
   
    0
    len(xs)
    i=1
    while i < len(xs):
        while i < len(xs) and xs[i] == xs[i-1]:
            i += 1
        xs.insert(i, 0)
        i += 1
    # Initialize result as the first coefficient and subtract one after each iteration
    result = xs[0]
    for i in range(1, len(xs)):
        result = result - xs[i]
    # Return the first non-zero result
    return result

def test_find_zero():
    """
    Test function to evaluate find_zero
    test_list = [1, 2, -6, 11, -6, 1]
    result = find_zero(test_list)
    assert result == 0
    assert result == test_list[0]

# Run the test function to check your implementation
    test_find_zero()

```

The function find_zero takes in a list of coefficients and returns the x-value at which the polynomial equals zero. The test_find_zero function tests whether the function returns the correct result for a known list of coefficients.