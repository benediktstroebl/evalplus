```python
def greatest_common_divisor(a, b):
    if b == 0:
        return a
    return greatest_common_divisor(b, a % b)
```
This recursive approach is quite efficient and wastes no time even for large inputs since each iteration has a constant workload. The correctness is induced by the fact that the greatest common divisor of integers `a` and `b` is the same as the greatest common divisor of `b` and `a % b`. This property can be intuitively understood as the factor 'b' being common to the original pair 'a' and 'b' if and only if it is also common to the pair 'b' and 'a % b'.