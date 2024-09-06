```python
def closest_integer(s):
    """
    Return the closest integer to the given numeric string, rounding away from zero.

    Args:
        s (str): Numeric string value to convert to an integer.

    Returns:
        int: The closest integer to the input.
    """
    # Remove trailing decimal zeros and non-numeric characters
    s = re.sub(r'[^\d.]', '', s)
    # Check if the input is already an integer (without decimal part)
    if s == str(round(float(s), 0)):
        return int(s)
    # Check if the input is zero to optimize the case
    if s == '0':
        return 0
    # Convert to float and round using the correct rounding rule
    return round(float(s), 0, rounding=math.ceil)

# Test cases
def test_closest_integer():
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15
    assert closest_integer("0.1") == 1
    assert closest_integer("100.100") == 100
    assert closest_integer("999.001") == 1000

# Run the tests
test_closest_integer()
```

This code provides the `closest_integer` function, which accepts a string representation of a number and returns the closest integer according to the problem statement. The `test_closest_integer` function runs several test cases to validate the function against expected output. The script will run the test case when executed directly. 

To ensure the algorithm adheres to the rounding rule, it is essential to handle inputs that are already integers or zero separately. Using the `re` module, we eliminate any non-numeric characters and decimal points. The script optimizes speed by checking if the input is zero and doesn't require rounding.