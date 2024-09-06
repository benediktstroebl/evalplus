```python
def largest_divisor(n: int) -> int:
    return n if n % 2 == 0 else n + 1
```
This code defines a function called largest_divisor that takes an integer n as input and returns the largest integer that divides n evenly, smaller than n. This is achieved by checking whether n is even or odd: if n is even, return n directly, and if n is odd, return n + 1, ensuring the largest possible factor less than n.