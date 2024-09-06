```python
import math
def find_zero(xs):
    assert len(xs) % 2 == 0
    assert max(abs(xs[i]) for i in range(len(xs))) <= 1
    return math.pow(min(xs))
```
Do you need help with anything else?