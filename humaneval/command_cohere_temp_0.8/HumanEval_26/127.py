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

The following tests evaluate the function:
```python
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([1, 1, 2, 3, 4, 4, 2, 2]) == [1, 2, 3, 4]
    assert remove_duplicates([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]) == [0, 1, 2, 3, 4]
```

The function uses a set, `seen`, to keep track of elements that have been encountered before. A list comprehension is then used to filter the numbers that are not in the `seen` set, thereby removing duplicates. As stated in the docstring, the function preserves the order of the remaining elements. This is achieved by using a list comprehension instead of a set, which retains the order of the elements from the original list.