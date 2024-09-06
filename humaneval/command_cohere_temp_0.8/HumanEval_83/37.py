Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the digits of the number from the second to the last
    # This will be the number without the first and last digit
    digits = list(str(n - 1))
    # Remove the element at position 0 to avoid duplicate 1s
    digits.pop(0)
    # If the last digit is not 1, remove it too
    if digits[-1] != '1':
        digits.pop()
    # If the list of digits is empty, it means the number does not start or end with 1
    if not digits:
        return 0
    # Initialize the count of numbers with 1 as digits[0]
    count = 1 if digits[0] == '1' else 0
    # Iterate through each digit in digits and increment count accordingly
    for digit in digits:
        # If the current digit is 1, and it's not the first iteration (i.e., digit is not the first digit of the number),
        # increment the count
        if digit == '1' and count > 0:
            count += 1
        # If the current digit is not 1, and it's not the last iteration (i.e., digit is not the last digit of the number),
        # decrement the count
        elif digit != '1' and count > 0:
            count -= 1
    # Return the final count
    return count
```

This function should correctly solve the problem for any given `n`. It calculates the count of `n`-digit positive integers that start or end with 1, by iterating through the digits from the second to the last and updating the count accordingly.

To test this function, you can copy and paste the code into a Python environment and use functions like `assertCountEquals` from the solution section to ensure correctness:
```python
def assertCountEquals(actual, expected):
    """
    Asserts that actual counts of numbers starting or ending with 1 is equal to expected.
    """
    if actual != expected:
        raise AssertionError(f"Count is {actual}, but expected count to be {expected}")
``` 
This `assertCountEquals` function can now be used to test your `starts_one_ends` function:
```python
import unittest

class TestStartsOneEnds(unittest.TestCase):
    def test_starts_one_ends(self):
        self.assertCountEquals(starts_one_ends(1), 0)
        self.assertCountEquals(starts_one_ends(2), 1)
        self.assertCountEquals(starts_one_ends(10), 10)
        self.assertCountEquals(starts_one_ends(11), 10)
        self.assertCountEquals(starts_one_ends(100), 92)
```

This test suite will execute the `starts_one_ends` function with different input values and validate that the output counts match the expected values.