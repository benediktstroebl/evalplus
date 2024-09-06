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