from typing import List, Tuple
def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    return [max(subsequence) for subsequence in zip_longest(numbers, numbers[1:], fill_value=0) for max_ in 
           map(max, subsequence)]
def zip_longest(*args, fill_value=None):
    """Zip longest iterations over iterables in argument and return a tuple of longest iterables in input."""
    stop = False
    itrs = [iter(arg) for arg in args] + [iter([fill_value])] * (len(args) - 1)
    result = []
    while not stop:
        result.append(next(itrs.pop(0)))
        stop = all(not _ for _ in itrs)
    return tuple(result)
numbers = [1, 2, 3, 2, 3, 4, 2]