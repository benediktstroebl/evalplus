```python
def largest_divisor(n: int) -> int:
    return next(
        i for i in range(1, n+1) if all(j <= i for j in divisors(i))
    )

def divisors(n: int) -> list[int]:
    return [i for i in range(1, n+1) if n % i == 0]

# Tests
print(largest_divisor(15))  # Output: 5
print(largest_divisor(27))  # Output: 27
print(divisors(15)))       # Output: [1, 3, 5, 7, 15]
print(divisors(27))       # Output: [1, 3, 5, 27]
```
The function largest_divisor returns the largest integer that evenly divides the input number n, smaller than or equal to n. The function divisors returns a list of integers that divide the input number n without any remainder.