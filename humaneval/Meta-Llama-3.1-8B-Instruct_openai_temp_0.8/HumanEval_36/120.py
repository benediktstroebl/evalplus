```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit for the search.

    Returns:
        int: The count of occurrences of the digit 7.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Example use cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines the `fizz_buzz` function, which iterates over integers less than the given number `n`. For each integer, it checks if it's divisible by 11 or 13. If it is, it counts the occurrences of the digit 7 in the integer's string representation and adds the count to the total. The function returns the total count.