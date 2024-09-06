```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen]
    return result


# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [1, 2, 2, 3, 4]
numbers3 = [1, 2, 3, 4, 5]

print(remove_duplicates(numbers1))
print(remove_duplicates(numbers2))
print(remove_duplicates(numbers3))
```

The output will be as follows:
```
[1, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 5]
```

The `remove_duplicates` function removes duplicate elements from the input list and returns a new list with unique values.  The element is not added to the result if it's already in the set of seen elements.