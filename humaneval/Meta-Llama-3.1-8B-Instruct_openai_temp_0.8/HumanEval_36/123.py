```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in numbers from 1 to n.
    """
    return sum(str(i).count('7') for i in range(1, n+1))


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    return sum(count_sevens(i) for i in range(1, n) if i % 11 == 0 or i % 13 == 0)


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script first defines a function `count_sevens(n)` which counts the occurrences of the digit 7 in numbers up to `n`. It then uses a generator expression to apply this function to all numbers in the range from 1 to `n-1` that are divisible by 11 or 13, and sums up the results to get the total count of 7's in those numbers.