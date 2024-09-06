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

The function `remove_duplicates` removes elements that occur more than once in a list of integers while maintaining the order of the remaining elements. It does so by using a set, `seen`, to keep track of elements already encountered, and appends elements to a `result` list if they have not been previously seen or if they are the first occurrence of an element. 

Here is an example usage of the function:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```

This approach has a time complexity of `O(n log n)`, where `n` is the length of the input list, due to the set operations, and uses linear space in the result list.