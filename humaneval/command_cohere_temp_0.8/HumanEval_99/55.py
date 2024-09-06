```python
def closest_integer(s):
    """
    Return the closest integer to the given value, rounding away from zero.

    Args:
        s (str): The value to convert to an integer.

    Returns:
        int: The closest integer to the given value.
    """
    n = float(s)
    i = int(n)
    near_zero = abs(n - i) < 1e-5 and n > 0 and n < 1
    return i if near_zero else n if n % 1 == 0 else n + np.sign(n)

# Test cases
cases = [
    ("10", 10),
    ("15.3", 15),
    ("14.5", 15),
    ("-14.5", -15),
    ("17.999999", 18),
    ("-17.999999", -18),
]

for input, expect in cases:
    actual = closest_integer(input)
    assert actual == expect, f"Failed input: {input}, Expected: {expect}, Actual: {actual}"
```

In the function `closest_integer`, we first convert the string value to a float and then to an integer. We use the `np.sign()` function from the NumPy library to determine the sign of the floating-point value, and add this sign to the value to round away from zero if necessary.

The test cases check if the function behaves as expected for different inputs. You can run this code to verify the correctness of the `closest_integer` function. Note that you'll need the NumPy library installed to run this code.

To execute the code, you would need to install NumPy via `pip install numpy` and then copy and paste the code into a Python interpreter or a script file (e.g., `closest_integer.py`) and run using the command `python closest_integer.py`.