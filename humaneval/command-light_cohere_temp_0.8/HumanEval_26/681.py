```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen]
    seen.add(numbers)
    return result

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
The provided Python script defines a function remove_duplicates that takes a list of integers as input and aims to remove duplicate occurrences. It utilizes a unique element technique to construct a set of seen elements and uses list comprehension to filter out elements that are not in the set, resulting in a new list containing unique integers. The script then tests the unique elements and prints the result.