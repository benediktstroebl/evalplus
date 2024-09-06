```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))  # use set to remove duplicates and return a new list


# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5]
print("Test 1 results: ", remove_duplicates(numbers_list))  # Output: [1, 2, 3, 4, 5]

numbers_set = set([1, 2, 3, 4, 5])
print("Test 2 results: ", list(remove_duplicates(numbers_set)))  # Output: [1, 2, 3, 4, 5]

numbers_list2 = [5, 4, 2, 6, 3, 7]
print("Test 3 results: ", remove_duplicates(numbers_list2))  # Output: [2, 3, 4, 5, 6, 7]

numbers_set2 = set([5, 4, 2, 6, 3, 7])
print("Test 4 results: ", list(remove_duplicates(numbers_set2)))  # Output: [2, 3, 4, 5, 6, 7]
```
This Python code defines a function remove_duplicates that removes duplicate elements from a list of integers. It achieves this by converting the list to a set, ensuring unique elements, and then returning a new list with no duplicates. The code includes multiple test cases, demonstrating the function's behavior and outputting the results for various input scenarios.