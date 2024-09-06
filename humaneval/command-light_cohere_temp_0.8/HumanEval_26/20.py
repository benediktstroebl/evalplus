```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen]
    seen.add(numbers)
    return result

# Test cases
numbers = [1, 2, 3, 2, 4]
test_numbers = [5, 6, 7, 6, 8]

results = remove_duplicates(numbers)
test_results = remove_duplicates(test_numbers)

print("Original list:", numbers)
print("List without duplicates:", results)
print("Test list:", test_numbers)
print("List without duplicates:", test_results)
```
This Python script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. The function utilizes a set data structure to track elements seen before and creates a new list containing only unique elements. The test cases demonstrate the basic usage of the function, passing both a list of integers and a list of test numbers. This demonstrates how the