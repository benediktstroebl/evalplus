from typing import List
def fibfib_list(n: int) -> List[int]:
    fibfib = [0, 0, 1]
    while len(fibfib) <= n:
        fibfib.append(sum(fibfib[-3:] + [fibfib[-1]]))
    return fibfib
def fibfib(n: int) -> int:
    return fibfib_list(n)[-1]