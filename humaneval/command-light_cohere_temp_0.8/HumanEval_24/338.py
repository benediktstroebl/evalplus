```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if not n % d and divisible(n, d)), n)

def divisible(n: int, d: int) -> bool:
    return n % d == 0 and d <= n

def test_largest_divisor():
    assert largest_divisor(5) == 5
    assert largest_divisor(10) == 5
    assert largest_divisor(12) == 4
    assert largest_divisor(20) == 4
    assert largest_divisor(40) == 4

    assert divisible(10, 5)
    assert divisible(30, 15)
    assert divisible(100, 25)

if __name__ == "__main__":
    test_largest_divisor()
``` 
This code defines a function `largest_divisor(n)` that returns the largest integer which divides `n` without a remainder and smaller than `n`. It employs a list comprehension to find all such divisors, and then returns `n` if no such divisors are found. The `divisible(n, d)` function returns `True` if `n` is divisible by `d`, and `d` is less than or equal to `n`. The `test_largest_divisor()` function tests the correctness of the `largest_divisor` function with various inputs. 
Then, the `if __name__ == "__main__"` block ensures that the function is executed when the script is run directly, rather than being imported elsewhere.