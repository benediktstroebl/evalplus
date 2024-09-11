```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily access individual digits
            str_i = str(i)
            # Count the number of times the digit 7 appears
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script works by iterating over all numbers from 1 to `n-1`, checking if each number is divisible by 11 or 13, and if so, counting the number of times the digit 7 appears in that number. It returns the total count.

Note: This script has a time complexity of O(n) because it checks every number up to `n-1`. If `n` is very large, this could be slow. However, since the problem statement does not specify any specific performance requirements, this simple solution should be sufficient.