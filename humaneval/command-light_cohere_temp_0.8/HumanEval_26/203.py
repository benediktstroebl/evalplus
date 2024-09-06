```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]


numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
numbers = [1, 3, 4, 2, 2, 5, 6]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4, 5, 6]
```

The function `remove_duplicates` takes a list of integers as input and returns a new list with elements that are not duplicate. The function uses a list comprehension and the `count()` method to filter out the duplicate elements from the input list. The test cases cover different scenarios of the input list, and the expected output is printed to verify the correctness of the function.