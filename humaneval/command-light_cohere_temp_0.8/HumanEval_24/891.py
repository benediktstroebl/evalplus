```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not divisible(n, d)))

def divisible(n: int, d: int) -> bool:
    return n % d == 0

def test_largest_divisor():
    n = 15
    assert largest_divisor(n) == 5
``` 
This script defines a function `largest_divisor` that returns the largest divisor of a given number `n`. It employs a generator expression to find this divisor, ensuring that it will return the largest value that does not create a division by 0.  The test function `divisible` that checks if a given number `n` is divisible by a given divisor `d`, and returns `True` if they are divisible and `False` otherwise.  Finally, the tests this `largest_divisor` function by passing the number 15 to it and asserts that the result is equal to 5, which is the correct behavior.