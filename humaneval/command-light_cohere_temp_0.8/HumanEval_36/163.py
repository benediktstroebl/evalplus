Here is a self-contained Python script that defines a function `fizz_buzz` that solves the problem of counting the number of times the digit 7 appears in integers less than a given number which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
   >>> 
    It MATHS DECLARATION
    >>> import math
    >>> n = int(input("Enter a number: "))
    >>> solution = math.floor(math.sqrt(1.0 * (n + 7))
    - 7
    - math.floor(math.sqrt(1.0 * (n -
    5))
    - math.floor(math.sqrt(1.0 * (n) + 2))
    - math.floor(math.sqrt(1.0 * (n) + 5))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 8))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 9))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 10))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 11))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 12))
    - 7
    - math.floor(math.sqrt(1.0 * (n) + 13))
    - 7
    """
    return solution

# TESTS
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    >>> fizz_buzz(82)
    4
    >>> fizz_buzz(60)
    6
    >>> fizz_buzz(81)
    8
    """