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

This approach uses a set `seen` to keep track of already seen integers. The resulting list `result` is returned as described in the problem statement. The tests provided for this function would likely include at least the following:
```python
# test whether the result is correct for a simple example
assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

# test whether the result is correct for a more complex example
assert remove_duplicates([10, 9, 2, 5, 2, 3, 4, 7, 8, 10]) == [10, 9, 2, 5, 3, 4, 7, 8]

# test whether input shape is preserved
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
```