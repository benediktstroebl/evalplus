```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in [x for x in numbers if x in seen]]

	# Test cases
test_remove_duplicates = [
    [1, 2, 3, 2, 4],
    [1, 3, 4, 2, 2, 5],
    [10, 10, 20, 30, 40, 10],
    [100, 200, 300, 100]
]

	for test_set in test_remove_duplicates:
		remove_duplicates(test_set)
		print(test_set, "after remove duplicates:", end='')
		print()
```
This script defines a function `remove_duplicates` that removes duplicate numbers from a given list, and then tests the function with several input lists. It uses a particular data structure to keep track of the seen numbers, then iterates through the input list, and adds numbers to the set if they are not already seen. The output will show the expected unique numbers.