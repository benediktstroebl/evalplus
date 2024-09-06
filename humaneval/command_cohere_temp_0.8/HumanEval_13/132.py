```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The GCD method uses Euclid's algorithm inherently and decreases the larger number's magnitude progressively. It is efficient and utilizes a recursive approach to determine the greatest common divisor.