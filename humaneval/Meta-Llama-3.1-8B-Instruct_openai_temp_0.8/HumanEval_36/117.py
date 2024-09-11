```python
def count_sevens(n: int) -> int:
    """Count the occurrences of the digit 7 in numbers less than n that are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if (i % 11 == 0) or (i % 13 == 0):
            str_i = str(i)
            count += str_i.count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return count_sevens(n)

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script works as follows: 

1. The function `count_sevens(n)` loops over all integers less than `n`. 
2. For each integer `i`, it checks if `i` is divisible by 11 or 13.
3. If `i` is divisible, it converts `i` to a string, counts the occurrences of the digit 7, and adds this count to the total count.
4. The function `fizz_buzz(n)` simply calls `count_sevens(n)` and returns its result. 

In the test section, the script prints the results of `fizz_buzz(n)` for `n=50`, `n=78`, and `n=79`.