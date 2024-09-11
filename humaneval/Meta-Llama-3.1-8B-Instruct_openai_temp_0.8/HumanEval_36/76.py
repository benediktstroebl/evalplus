```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n - 1, 0, -1):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count

# Test cases
if fizz_buzz(50) == 0:
    print("Test case 1 passed")
if fizz_buzz(78) == 2:
    print("Test case 2 passed")
if fizz_buzz(79) == 3:
    print("Test case 3 passed")
```

This script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It does this by iterating over the range from `n-1` to 1 in reverse order, checking each number to see if it's divisible by 11 or 13, and if so, counting the occurrences of the digit 7 in the string representation of the number. The test cases at the end ensure that the function works correctly for the given examples.