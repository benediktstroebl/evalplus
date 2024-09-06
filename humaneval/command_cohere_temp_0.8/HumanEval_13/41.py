```python
def greatest_common_divisor(a, b) -> int:
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient for larger integers since it achieves a time complexity of O(log(min(a, b))). This is a reduction from a worst-case time complexity of O(log(abs(a)) + log(abs(b))) for an iterative approach. The idea behind the algorithm is to repeatedly divide the larger number by the smaller one and keep doing this until the smaller number becomes zero. At each step, the largest number that can divide both numbers evenly is the greatest common divisor.