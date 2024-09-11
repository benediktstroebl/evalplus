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
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script uses a for loop to iterate over all integers from 1 to `n-1`. It checks each integer to see if it is divisible by 11 or 13 using the modulus operator (`%`). If it is, it converts the integer to a string and uses the `count` method to count the number of times the digit 7 appears. It then adds this count to the total count. Finally, it returns the total count.