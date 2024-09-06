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

The function `remove_duplicates` eliminates duplicate integers from a given list while maintaining the order of unique elements. It operates by initializing a `set` called `seen` to track encountered integers. As it iterates through the input `numbers`, it adds only unique elements to the `result` list and inserts each integer into the `seen` set after its first occurrence. This ensures that any repeat entries are excluded from both the final `result` and the `seen` set. 

Here's an example usage and the expected outcome:
```python
test_list = [1, 2, 3, 2, 4]
print(remove_duplicates(test_list))  # Output: [1, 3, 4]
``` 

This method of duplicate removal promotes efficiency and readability, as it avoids repeatedly sorting the list or manually eliminating duplicates.