```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient for larger integers as it constantly reduces the smaller of the two integers to zero while gradually increasing the other integer. The base case of the recursion is when the second integer becomes zero, at which point the greatest common divisor is the first integer itself.