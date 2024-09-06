```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    return [max(subsequence) for subsequence in zip_longest(numbers, numbers[1:], fill_value=0) for max_ in 
            map(max, subsequence)]

def zip_longest(*args, fill_value=None) -> List[Tuple[int]]:
    """Zip longest function taken from (https://stackoverflow.com/questions/137605/zip-longest-shortest-python)"""
    # We create an iterator which will zip the shortest iterable with the default value
    result = (tuple(fill_value if len(i) == 0 else x for i, x in enumerate(iterable))
             for iterable in args)
    # Now we zip the iterables with the fill value and ourselves as the key
    return list(zip_longest_impl(result, fill_value=fill_value, key=id))

def zip_longest_impl(iterable, fill_value=None, key=None):
    """The actual implementation."""
    args = sorted(iterable, key=key)
    if not args:
        return []
    result = itertoolz.zip_longest(*args, fill_value=fill_value)
    return list(result)
```