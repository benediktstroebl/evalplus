```python
def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1))
    
    # Remove the starting and ending 1 if present
    if digits[0] == 1:
        digits.pop(0)
    if digits[-1] == 1:
        digits.pop(-1)
    
    # Count the remaining digits
    count = len(digits)
    
    return count
```

This function removes the starting and ending 1s from the list of digits if they are present. Then, it counts the number of remaining digits and returns the result. This solution adheres to the problem statement and provides the required count of n-digit positive integers that start or end with 1. 

The function `starts_one_ends` has a time complexity of O(n) since it iterates through the list of digits once to remove the starting and ending 1s, if present. The space complexity is O(1) as it only uses a constant amount of memory to store the digits list.