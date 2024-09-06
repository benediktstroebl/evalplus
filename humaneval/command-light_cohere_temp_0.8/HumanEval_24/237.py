Here's a self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    while any(divisible for div in range(1, n+1) if n % div == 0):
        div = min(div for div in range(1, n+1) if div != n and div % n == 0)
    return div
```
This function uses a while loop to iterate through numbers from 1 to the given number n, and checks each number if it divides n exactly. If any such divisors are found, the smallest such divisor is returned.

This solution is self-contained, meaning it does not rely on the global scope or external functions/classes. It is the best way to solve the problem within a small function, ensuring readability and maintainability.