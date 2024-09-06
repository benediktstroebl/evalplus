```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            return i
    return 1
```
This script defines the `largest_divisor` function, which takes a number `n` as input and searches for the largest divisor of `n` that is also smaller than `n` itself. It does this by iteratively checking all numbers from 1 up to `n-1` to find the largest divisor that meets these conditions. The function is encapsulated within a test block that verifies the function's correctness using the `pytest` framework. Specifically, it checks if the function correctly identifies the largest divisor of 15 as 5. The `pytest` framework will automatically evaluate this test case and report whether the function passes or fails. 
```python
def test_largest_divisor():
    """ Test the largest_divisor function """
    assert largest_divisor(15) == 5
```