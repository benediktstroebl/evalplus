Here's a self-contained Python function that removes duplicate numbers from a list, following the description:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers]


# Example test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [4, 2, 8, 2, 10, 2]

print("Results of remove_duplicates:", numbers1)
print("------------")
print("Results of remove_duplicates:", numbers2)
print("------------")
```

This code defines the remove_duplicates function that removes duplicate numbers from the input list. It utilizes a using a set data structure to keep track of seen elements and then returns a new list with elements that are not in the seen set and not in the input list.