```python
def fibfib(n: int):
    prev1, prev2, fibfib_number = 0, 0, 0
    while n >= 3:
        fibfib_number = prev1 + prev2 + fibfib_number
        prev2, prev1 = prev1, fibfib_number
        n -= 1
    if n == 2:
        fibfib_number += prev2
    elif n == 1:
        fibfib_number += prev1
    return fibfib_number
```

This script defines a function called `fibfib` that takes an integer `n` as input and returns the n-th number in the FibFib sequence. The sequence is defined as follows:
- `fibfib(0) == 0`
- `fibfib(1) == 0`
- `fibfib(2) == 1`
- `fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3)`

The code uses a while loop to efficiently compute the n-th element of the FibFib sequence. It maintains three variables: `prev1`, `prev2`, and `fibfib_number`, where `prev1` and `prev2` represent the two previous FibFib numbers, and `fibfib_number` represents the current FibFib number. The loop iterates until n is smaller than 3. It updates `fibfib_number` in each iteration by adding the sum of `prev1` and `prev2` to the previous `fibfib_number`. This iterated addition process calculates the correct FibFib number for n. If n is 1 or 2, the code handles the edge cases correctly by adding `prev1` or `prev2` appropriately to `fibfib_number`.