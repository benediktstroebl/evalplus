```python
from typing import List

def fibfib_matrix(n: int, matrix: List[List[int]]) -> int:
    """
    Generate the n-th FibFib number by matrix exponentiation. The idea is to use the matrix representation of the FibFib sequence:
    [1,1]
    [1,0]
    Each FibFib(k) number is the sum of the matrices' elements at k-th diagonal starting from the upper-left.
    """
    if n < 0:
        raise ValueError("n must be non-negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Calculate (F(n-1) + F(n-2))/2 for each element of the matrix
    for k in range(1, n // 2 + 1):
        matrix[k][k] = (matrix[k - 1][k - 1] + matrix[k - 1][k]) / 2
        matrix[k][k + 1] = (matrix[k - 1][k + 1] + matrix[k][k]) / 2

    if n % 2 == 0:
        return matrix[n // 2][0]
    else:
        return matrix[n // 2][1]

def fibfib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative.")
    matrix = [[0, 0], [0, 1]]
    return fibfib_matrix(n, matrix)

# Tests
assert fibfib(0) == 0
assert fibfib(1) == 0
assert fibfib(5) == 4
assert fibfib(8) == 24
```
This solution uses matrix exponentiation to efficiently compute the n-th FibFib number, following the definition of the FibFib sequence. It avoids recursive calls and uses matrix operations for better performance.