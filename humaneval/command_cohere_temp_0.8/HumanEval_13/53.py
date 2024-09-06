```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This algorithm utilizes Euclid's algorithm to find the greatest common divisor between two integers `a` and `b`. It optimizes the computation by reducing the recursive calls' magnitude, ultimately reaching a base case where `b` is 0. At this point, it returns `a` since `a` is the divisor for `b` equal to 0. This approach drastically reduces the maximum number of recursive calls to only ~ log(min(a, b)) iterations, making it much more efficient than a straightforward recursive implementation.