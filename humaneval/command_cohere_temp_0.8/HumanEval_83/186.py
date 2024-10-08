Here's a Python script with a self-contained function `starts_one_ends` that solves the problem as described in the markdown code block:
```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list to store the digits from 0 to n-1.
    digits = list(range(0, n))
    
    # Handle the edge case where n = 1
    if n == 1:
        return 1
    
    # Handle the case where n is even and starts with 1 and ends with 1
    if n % 2 == 0 and digits[0] == 1 and digits[n - 1] == 1:
        return 1
    
    # Initialize the count of numbers starting or ending with 1.
    count = 0
    
    # Remove the leading and trailing 1 if present
    # and increment the count if true
    if digits[0] == 1:
        digits.pop(0)
        count += 1
    if digits[-1] == 1:
        digits.pop(-1)
        count += 1
    
    # Iterate over the remaining digits to construct valid numbers.
    for i in range(len(digits)):
        current_number = int('1' + ''.join(map(str, digits)) + '1')
        if current_number >= 10 ** (n - 1) and current_number <= 10 ** n:
            count += 1
    
    return count
```

This script defines the function `starts_one_ends` which takes a positive integer `n` as input and returns the count of `n-digit` positive integers that start or end with 1. The script handles the edge cases and increments the count based on the presence of 1 in the starting or ending positions. It then constructs all the combinations of digits and checks if they form a valid number in the given range to increment the count.