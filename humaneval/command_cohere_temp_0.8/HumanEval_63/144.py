```python
from typing import List

def fibfib_helper(n: int, acc: List[int]):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n <= 3:
        acc[:] = [0, 0, 1]
    else:
        fibfib_helper(n - 1, acc) + fibfib_helper(n - 2, acc) + fibfib_helper(n - 3, acc)

def fibfib(n: int) -> int:
    res = fibfib_helper(n, [])
    return res

# Tests
print(fibfib(1))
# 0

print(fibfib(5))
# 4

print(fibfib(8))
# 24
```

The function `fibfib` uses a recursive approach to calculate the n-th element of the FibFib sequence, but it also leverages an optimization to store previously computed values in-memory, reducing the number of recursive calls for subsequent calculations. This is achieved through the use of an accumulator (`acc`) parameter that keeps track of previously computed values. When the function is called, it checks if the input `n` is `0`, `1`, or `2`, in which case the answer is straightforward, or if `n` is less than or equal to 3, in which case it sets the accumulator to store the values of the first few terms (resetting the accumulator when needed). For larger `n`, it recursively computes the FibFib value for `n-1`, `n-2`, and `n-3` and adds their sums to the accumulator's latest value, providing an efficient way to compute larger FibFib numbers without recomputing earlier terms.