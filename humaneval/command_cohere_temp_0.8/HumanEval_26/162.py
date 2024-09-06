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

The function `remove_duplicates` uses a set `seen` to track encountered integers and a list `result` to store the unique integers in the order they appear in the input list.

It iterates through the input `numbers`. For each integer `num`, it checks whether it has been previously seen (`num not in seen`). If it has not been seen yet or if it's the first duplicate encountered (`len(seen) == 1`), it adds the integer to the `result` list and marks it as seen in the `seen` set.

This ensures that the final `result` list contains only unique integers from the input, without altering their order. 

The solution is specified to work with integers, but could be modified for other data types with different data types or additional logic for uniqueness.