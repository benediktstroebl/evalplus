Here is a self-contained Python script that defines a function `fizz_buzz` solving the problem of counting the number of 7s in integers less than a given number that are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    >>> fizz_buzz(81)
    0
    >>> fizz_buzz(90)
    0
    >>> fizz_buzz(105)
    1
    """

    def count_7s(num):
        divisible = num % 11 == 7 or num % 13 == 7
        return (divisible)

    return count_7s(n)
```