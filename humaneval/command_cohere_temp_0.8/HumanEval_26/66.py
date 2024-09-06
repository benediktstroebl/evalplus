```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input
    """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

The algorithm is a typical `set`-based approach. It iterates through the list of numbers, using a `for` loop. For each number, it checks whether it has already been seen (i.e., is in the `seen` set). If so, it skips that number. If not, it adds the number to the `seen` set and retains it in the `result` list. This way, the final `result` list only contains unique elements from the original input.

The code is generic and can be applied to any scenario involving removing duplicate elements from a list while preserving order. It is also efficient, with a time complexity of `O(n)` because it has to traverse the input list only once and performs minimal additional operations per element.