Here is a self-contained Python script with a function that solves the problem of finding the largest number that divides a given number evenly:
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
This script defines a function called largest_divisor, which takes an integer n as input and returns the largest integer that divides evenly into n, smaller than n. This function uses the game theory to find the answer. It starts iterating through numbers from 1 to n+1 and checks if the remainder of n divided by each number is 0. The first number that satisfies the condition, so it is returned as the answer.