Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the prompt:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the digits from 0 to 9.
    digits = list(range(10))
    # Remove the 1st digit from the list, as the numbers starting or ending with 1
    # have 1 as the first or last digit, which is already covered.
    digits.remove(1)
    # If there are no digits left, return 0.
    if not digits:
        return 0
    # Initialize the count of valid numbers.
    count = 0
    # Loop through lengths from 1 to n.
    for length in range(1, n + 1):
        # Loop through the remaining digits.
        for digit in digits:
            # Concatenate the digit to construct numbers of the desired length.
            number = str(digit) * length
            # Check if the number starts or ends with 1.
            if number.startswith('1') or number.endswith('1'):
                count += 1
    return count
```

This code creates a function `starts_one_ends` that takes a positive integer `n` as input and returns the count of n-digit positive integers that start or end with 1. The solution leverages the fact that the count of digits from 0 to 9 is `10`, and removes the `1` as it is both the starting and ending digit. The solution then iterates through lengths from 1 to `n` and loops through the remaining digits to construct potential n-digit numbers. It checks if each constructed number starts or ends with 1 and increments the count accordingly.