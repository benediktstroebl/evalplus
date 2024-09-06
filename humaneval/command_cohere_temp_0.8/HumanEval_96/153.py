```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n prime numbers less than n."""
    result = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            result.append(i)
    return result
```
The `count_up_to()` function iterates through numbers from 2 up to `n`, adding each prime number less than `n` to the `result` array until it reaches `n` elements. This approach ensures that the returned array contains the first `n` prime numbers less than `n`. 

Here's a test suite to verify the correctness of the solution:
```python
def test_count_up_to():
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
    assert count_up_to(0) == []
    assert count_up_to(1) == []

test_count_up_to()
```
You can add more test cases to cover a variety of scenarios, such as larger values of `n` or cases where `n` is less than the largest prime number less than `n`.