```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if n % d == 0))
```
This code defines a function named largest_divisor that takes an integer n as input and returns the largest integer that evenly divides n. The function uses the above for loop to iterate through numbers from 1 to n (inclusive), and the condition n % d == 0 checks whether d is a divisor of n.

The function returns the first such divisor found, which is guaranteed to be less than n. 

The use of next allows the function to efficiently return the first divisor without the need for the user to manually advance the loop.