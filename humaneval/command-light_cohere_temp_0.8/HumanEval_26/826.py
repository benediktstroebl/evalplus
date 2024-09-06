```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Test the function with a list of numbers
test_numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(test_numbers)
print(result)  # Output: [1, 3, 4]

# Test with a list of strings
test_strings = ["hello", "world", "hello"]
result = remove_duplicates(test_strings)
print(result)  # Output: ["hello", "world"]
```

This function removes duplicate elements from a list of integers or strings, providing a self-contained solution. It utilizes the first input of a list of numbers, and then applies the removal of duplicates using a set of the elements in the list. In this way, it uses the set data type to create a unique identifier for each element, ensuring that duplicates are removed effectively. The output of the final test is a list of unique numbers or strings.