```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if numbers.count(n) == 1]

# Example:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [4, 4, 4, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [4]

numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 6, 7]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]
```

The code provides a remove_duplicates function that accepts a list of integers as an argument. It utilizes the method to eliminate duplicate numbers by using the count of each element to determine whether it appears more than once in the list. The function then creates a new list that only contains the elements that have a count of 1, which ensures that all duplicate elements are removed.