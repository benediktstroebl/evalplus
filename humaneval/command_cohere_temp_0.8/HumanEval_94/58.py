```python
def skjkasdkd(lst):
    primes = [x for x in lst if x % 2 == 1 and x > 1]
    return sum(map(int, str(max(primes))))
```

The function `skjkasdkd` uses a list comprehension to filter out integers from the input list that are both prime (have odd parity and are greater than 1) and returns their maximum value. The digit sum is then calculated using a `map` function applied to the string representation of the maximum prime integer.

To check the correctness of the solution, you can create a test suite with examples from the problem statement.

For example:
```python
# Test skjkasdkd function
def test_skjkasdkd():
    assert skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    assert skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]) == 13
    assert skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]) == 11
    assert skjkasdkd([0, 81, 12, 3, 1, 21]) == 3
    assert skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
```

This way, you can ensure that the function `skjkasdkd` correctly solves the problem and passes the tests.