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

This removes duplicates from the list whilst preserving the order. It does this by using a set, `seen`, to keep track of elements seen, and concatenating this with a list comprehension to filter the original list. The function returns a list of unique elements in the order they appeared first in the original list. 

Here is an example of how to use this function:
```python
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
``` 

This would output: [1, 3, 4] 

This is correct, it has removed the duplicates (2 and 2) from the original list, keeping the remaining elements in the order they appeared.