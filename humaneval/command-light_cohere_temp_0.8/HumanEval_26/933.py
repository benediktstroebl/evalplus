```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[seen:seen.new() <
[1, 2, 3, 4])
``` 
This Python function, `remove_duplicates`, takes a list of integers as input and removes all duplicate elements from it. It achieves this by creating a set of unique elements and then iterates through the original list, adding elements to the set if they are not already present. The function then constructs a unique list by filtering out any elements that are already present in the set.