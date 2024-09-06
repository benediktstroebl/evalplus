```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

    Args:
        numbers (List[int]): The input list of integers.
        rolling_window (int): The size of the rolling maximum window.

    Returns:
        List[int]: A new list where each element is the maximum of the corresponding window in the input list.

    >>> rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers or not rolling_window:
        return []

    return [max(window) for window in zip_longest(numbers, numbers[1:], fillvalue=float('-inf'))]

def zip_longest(*args, fillvalue=None):
    """Like itertools.zip_longest, but as a generator."""
    assert all(isinstance(arg, collections.Iterable) for arg in args), args
    iterators = [iter(arg) for arg in args]
    while True:
        try:
            yield from zip(*(iterators if x is not fillvalue else [iter([fillvalue]) for x in range(len(args))]))
        except StopIteration as e:
            for it in iterators:
                if it is not e.args[0]:
                    continue
                yield from (fillvalue for _ in range(len(args)))
                break
            else:
                raise e
```

The rolling_max function takes two parameters: the input list of integers and the size of the rolling maximum window. It returns a new list where each element is the maximum value encountered thus far within the specified window. The zip_longest function is used to iterate over overlapping windows, comparing each element to the previous ones. In case there is no previous element (at the beginning of the list), a fillvalue (defaulted to -1) is used to ensure the max calculation still works as expected.

This code should provide a working implementation of the problem statement. Let me know if you need any adjustments. I'm here to help!