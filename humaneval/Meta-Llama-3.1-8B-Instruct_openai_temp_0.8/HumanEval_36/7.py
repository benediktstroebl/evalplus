```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    :param n: The upper limit (exclusive).
    :return: The count of appearances of the digit 7.
    """
    count = 0
    for i in range(11, n, 11):
        # Convert the number to a string to easily check for the digit 7
        if '7' in str(i):
            count += 1
        # Also check for multiples of 13
        for j in range(13, n, 13):
            if i!= j and '7' in str(j):
                count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```