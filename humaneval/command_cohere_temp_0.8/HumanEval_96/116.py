```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n"""
    count = 0
    numbers = []
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            numbers.append(num)
            count += 1
            if count == n:
                break
    return numbers
```

This script defines the `count_up_to()` function that returns an array of the first `n` prime numbers that are less than `n`. The `is_prime()` function is also defined to check if a number is prime. 

Additionally, the script includes concise unit tests for the `count_up_to()` function that validate its behavior against specific examples from the problem statement, these tests are placed in a separate function called `test_count_up_to()`.

```python
def test_count_up_to():
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
    assert count_up_to(0) == []
    assert count_up_to(1) == []
```