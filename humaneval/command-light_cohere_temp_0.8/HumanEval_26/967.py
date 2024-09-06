```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.find(x)]

	# Test
numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
``` 
This function, `remove_duplicates`, takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of seen elements, then it iterates through the input list and adds elements to the seen set if they are not in the input list or already in the result.