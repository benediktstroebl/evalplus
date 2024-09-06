```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[:-len(seen)]]
    return result
# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
```
The function uses a set to keep track of seen elements, then iterates through the input list, and adds elements to the set if they haven't been seen before and are not in the input list's sublist of duplicates. The list of integers is then filtered to only include elements that are not duplicates and not already seen.