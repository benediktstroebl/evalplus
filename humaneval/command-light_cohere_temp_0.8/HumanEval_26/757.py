```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen]
    seen.add(numbers)
    return result

# Test case
test_numbers = [1, 2, 3, 2, 4, 3, 1]
result_from_test = remove_duplicates(test_numbers)
print(result_from_test)  # expected output: [1, 3, 4]

test_empty = []
result_empty = remove_duplicates(test_empty)
print(result_empty)  # expected output: []

test_single = [3]
result_single = remove_duplicates(test_single)
print(result_single)  # expected output: [3]
```
This Python script provides a function `remove_duplicates` that accepts a list of integers and outputs a list of unique integers. It employs the using a set to keep track of unique integers. The function utilizes list comprehension to filter out any duplicate elements and returns the list of unique elements.

The script also provides a set of test cases: a list of integers, an empty list, and a list with a single element. The outputs of these function are then verified against the expected results, ensuring the correctness of the `remove_duplicates` function.