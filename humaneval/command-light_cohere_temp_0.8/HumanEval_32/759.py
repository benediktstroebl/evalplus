```python
import math
def evaluate_polynomial(xs, x):
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert max(abs(xs[i] - 0) for i in range(len(xs) // 2)) == 0
    return xs[0]
xs = [1, 2]
x = 0.5
result = evaluate_polynomial(xs, x)
assert result == find_zero(xs)
print(result) # 1 + 2 * x
print(find_zero(xs))  # [0.5]
```