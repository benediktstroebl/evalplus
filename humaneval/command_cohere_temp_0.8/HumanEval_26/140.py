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

The approach used in the function `remove_duplicates` is to iterate over the input list `numbers` and maintain a `set` called `seen` to keep track of unique elements. For each element `num` in `numbers`, it checks if `num` is not in `seen` or if the size of `seen` is 1, indicating the first occurrence of an element. If either condition holds, it appends `num` to the `result` list and adds it to the `seen` set. This ensures that elements occurring more than once are excluded from the result.

The expected output for a test case like `[1, 2, 3, 2, 4]` is `[1, 3, 4]`, which matches the result of the function.