```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[0]]
    seen.add(numbers[0])
    return result

# Example test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers_list))  # expected output: [1, 3, 4]
numbers_set = {1, 2, 3, 4, 5}
print(remove_duplicates(numbers_set))  # expected output: []

```

This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function utilizes a set data structure to keep track of seen elements, then iterates through the input list and adds elements to the result list if they are not in the seen set and are not duplicates of the first element in the list.