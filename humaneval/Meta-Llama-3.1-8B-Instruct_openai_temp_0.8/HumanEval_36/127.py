```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Parameters:
    n (int): The upper limit of the range.

    Returns:
    int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test the function
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function `fizz_buzz(n)` that counts the number of times the digit 7 appears in the numbers less than `n` that are divisible by 11 or 13. It converts each number to a string, counts the occurrences of the digit '7', and sums up these counts to get the total count. The function is then tested with the provided examples.