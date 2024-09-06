```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
The GCD method uses Euclid's algorithm exceptionally implemented to accommodate negative numbers and integers dropping the deeper common factors.