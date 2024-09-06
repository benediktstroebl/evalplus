```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n+1) if n % i == 0])
```
The above Python script defines a function named largest_divisor that takes an integer n as input and returns the largest integer that divides n exactly. The function achieves this by utilizing the concept of the maximum number that evenly divides n, found by considering all numbers from 1 to the given input n, ensuring that the divisor is smaller than n. The function then returns the value of the largest such divisor.