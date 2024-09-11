### Fizz Buzz Function
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The count of digit 7 in multiples of 11 or 13.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
In this script, we start from 1 and iterate up to `n-1`. We check if the current number `i` is divisible by 11 or 13. If it is, we convert `i` to a string `str_i` and count the occurrences of '7' in it. This count is then added to the total count. Finally, we return the total count.