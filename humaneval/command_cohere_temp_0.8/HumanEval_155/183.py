Here's a Python script that contains a function called even_odd_count, defined to solve the problem:
```python
def even_odd_count(num):
    """Return the number of even and odd digits in the integer num."""
    # Convert num to a string
    num_str = str(num)
    # Initialize the count of even and odd digits to 0
    even_count = 0
    odd_count = 0
    # Iterate over each digit in the num_str
    for digit in num_str:
        # If the digit is even, increment the even_count
        if digit % 2 == 0:
            even_count += 1
        # If the digit is odd, increment the odd_count
        else:
            odd_count += 1
    # Return a tuple of even and odd counts
    return (even_count, odd_count)
```

To ensure the functionality of the function, the following tests can be used:
```python
# Test case for positive integers
assert even_odd_count(424) == (2, 2)

# Test case for negative integers
assert even_odd_count(-23) == (1, 2)

# Test case for integers with only one digit
assert even_odd_count(9) == (1, 1)

# Test case for integers with no digits (should return (0, 0))
assert even_odd_count(0) == (0, 0)

# Test case for integers with multiple digits
assert even_odd_count(125) == (1, 3)
```

This script will provide the counts of even and odd digits in num, and the test suite demonstrates the function's behavior for a variety of input cases. 
If there are any further questions or additional assistance is needed, please provide the details in the original prompt or clarify what other aspects of handling this problem in code should be reviewed.