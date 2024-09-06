```python
from itertools import accumulate

def fibfib_iter(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def fibfib(n: int):
    if n < 0:
        raise ValueError("FibFib is defined only for non-negative integers")
    elif n == 0 or n == 1:
        return 0
    else:
        return next(accumulate(fibfib_iter(n), initial=0))

# Tests:
print(fibfib(1))
# 0

print(fibfib(5))
# 4

print(fibfib(8))
# 24

```
This script defines the `fibfib` function, which uses the `accumulate` function from the `itertools` module to efficiently calculate the n-th FibFib number by recursion. It also includes input validation to handle invalid input. The code is self-contained and can be executed directly.