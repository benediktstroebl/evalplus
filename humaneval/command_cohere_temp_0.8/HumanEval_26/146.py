```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Keeps order of elements left the same as in the input """
    seen = set()
    result = [x for x in numbers if not (x in seen or seen.add(x))]
    return result
```

This approach utilizes a set `seen` to keep track of encountered integers in the input list `numbers`. The main list comprehension filters out elements that occur more than once, with the help of the `not (... or ...)` construct to alternatively check if an element `x` is not in the `seen` set or add it to the set. The resulting list is a combination of unique elements from the input list, retaining their original order.  This algorithm is efficient and has a time complexity of `O(n)`, where `n` is the length of the input list.