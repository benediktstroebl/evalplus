Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(window)) for window in zip_longest(numbers, numbers[1:]+[None], fillvalue=None)] \
        [:rolling_window]

def zip_longest(*args, fillvalue=None):
    """Repeat elements in *args* until the longest iterable is exhausted.
    Iterate through the result with the same iteration behavior as itertools.zip_longest.
    Examples
    --------
    >>> list(zip_longest('abc', ['a', 'b']))
    ['a', 'b', 'c']
    >>> list(zip_longest('abc', ['a', 'b', 'c']))
    ['a', 'b', 'c']
    >>> list(zip_longest('abc', ['a', 'b', 'c'], fillvalue='N'))
    ['a', 'b', 'c']
    >>> list(zip_longest( ('abc',), ['a', 'b', 'c'], fillvalue=('N', 0)))
    [('a',), ('b',), ('c',)]
    """
    fillers = [fillvalue]*(max(map(len, args)) - sum(map(len, args)) + 1)
    return itertools.zip_longest(*args, fillvalue=fillers)
```

This script defines a function called `rolling_max` which takes two arguments; a `List` of numbers and an integer `rolling_window`. The function returns a `List` of integers containing the rolling maximum elements found in the sequence up to the given moment. To achieve this, it uses a helper function called `zip_longest` which is also included in the script.

Note that the `zip_longest` function is used to iterate over the rolling windows, with the `fillvalue` parameter set to `None` to handle the initial window correctly. Then `max` function is used to determine the maximum element in each window. The `rolling_max` function uses `zip_longest` to create rolling windows of the same length as the given `rolling_window` argument, and selects only the windows which fit completely within the number sequence.