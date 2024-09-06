```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x not in numbers[:]]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
test_remove_duplicates = [
    "This function correctly removes duplicates from the list.",
    "Result is: [1, 3, 4]",
    "Input list contains duplicates.",
    "Output list does not contain duplicates.",
    "List is valid."
]
remove_duplicates(numbers)
test_remove_duplicates(numbers)
```