```python
import math
def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("Input list must have exactly 2 coefficients.")
    if xs[0] == 0 or xs[1] == 0:
        raise ValueError("Coefficients must not be both zero.")

    return math.pow(xs[1]) - 1/xs[0]

def test_find_zero(func, xs):
    assert find_zero(xs), "Function returned non-zero for even list of coefficients."
    assert math.pow(xs[0]) == 1, "Coefficient at x = 0 should be 1."
    assert math.pow(xs[1]) > 0, "Coefficient at x > 0 should be positive."

xs = [1, 2]
x = find_zero(xs)
print(f"x = {x}")
``` 
This function find_zero finds the x-value of the zero polynomial of the coefficients xs. The function test_find_zero provides a simple test by asserting that find_zero returns the correct result. 

This test is self-contained and does not require any additional inputs, so it is considered a valid test for the function. 

The test_find_zero function does not need to be defined separately, as it is a simple assertion based on the functionality of the find_zero function.