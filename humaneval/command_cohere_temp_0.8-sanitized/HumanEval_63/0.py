from typing import List
def fibfib_list(n: int) -> List[int]:
    fibfib = [0, 0, 1]
    while len(fibfib) <= n:
        fibfib.append(fibfib[-1] + fibfib[-2] + fibfib[-3])
    return fibfib
def fibfib(n: int) -> int:
    return fibfib_list(n)[-1]