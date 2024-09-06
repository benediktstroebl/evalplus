```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This GCD algorithm is a variant of Euclidean Algorithm with optimization for faster convergence. It repeatedly replaces the larger number by the remainder of the division of the larger number by the smaller number, gradually reducing the magnitude of the numbers while approaching the GCD of the two numbers.