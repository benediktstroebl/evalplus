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

The approach used is a combination of a loop and a set. The code iterates through each number in the list and uses the set to keep track of unique elements. If a number is not in the set or if the set contains only one element, it means that the current number is unique or the last duplicate of its kind, respectively. In either of these cases, the number is added to the `result` list and marked as seen in the `seen` set. This way, the code efficiently removes duplicates while preserving the order of unique elements. 
The unit tests for this code are also important for ensuring its correctness, as they verify that the function performs according to its specification for various inputs.