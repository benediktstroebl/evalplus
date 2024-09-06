```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0: return b
    return max(a // d for d in set(b) if d != 0)

# Example usage:
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
``` 
This code defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers `a` and `b`. The function first checks if `a` is equal to 0, in which case it returns `b`. Then, it uses a list comprehension to find the largest factor `d` in the range of factors of `b` (i. This is the in the process to find the largest factor, and finally returns the result.