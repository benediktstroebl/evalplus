Here's the self-contained Python function to find the largest divisor of a given number:
```python
def largest_divisor(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n
```
This function takes an integer `n` as input and iteratively divides it by 2 until it becomes odd, effectively finding the largest odd divisor smaller than n.