```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The approach employed by the provided `remove_duplicates` function involves maintaining a list of unique elements from the input list and a set of all unique elements encountered, starting with an empty set `seen`. As the function iterates through the input `numbers` list, each element `num` is appended to the `result` list and added to the set `seen`. If the element has already been added to the set, meaning it's a duplicate, it will not be added to the `result` list, since `len(seen) == 1` at this point, indicating this is the first encounter of this unique element, and it will be added to both the set and the list. This ensures that only elements encountered once are added to the `result` list, and the order is retained as in the original input list.  This problem can be solved in many other ways, such as using dictionaries or other set combinations.  This solution is simple and efficient, with a time complexity of O(n).  It also has a nice bonus of not needing any imported libraries besides typing.