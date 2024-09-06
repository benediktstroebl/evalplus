```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set(numbers)

    # Filter out duplicates from the input list
    numbers_list = [num for num in numbers if num in unique_numbers]

    return numbers_list


# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```
This function, named `remove_duplicates`, takes a list of integers as input and returns a new list with unique integers. The set data structure is used to store unique integers, and then this data is filtered from the input list to retain only unique numbers. The output of this function will be a list containing the unique integers from the input.