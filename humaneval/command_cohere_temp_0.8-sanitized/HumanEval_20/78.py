from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return _get_closest_pair_efficient(left, right)
def _get_closest_pair_efficient(a, b):
    if a == b or (a - b) < 1e-6 and (b - a) < 1e-6:
        return a, b
    mx = max(a, b)
    mn = min(a, b)
    cmn = (mx + mn) / 2
    cmx = (mn + mx) / 2
    acmn, bcmn = a - cmn, b - cmn
    acmx, bcmx = a - cmx, b - cmx
    if (abs(acmn) + abs(acmx)) < (abs(acmx) + abs(acmn)) and (abs(bcmn) + abs(bcmx)) < (abs(bcmx) + abs(bcmn)):
        return cmn, cmx
    else:
        return _get_closest_pair_efficient(cmn, cmx)