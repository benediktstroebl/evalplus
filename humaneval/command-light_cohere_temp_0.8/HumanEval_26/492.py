```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    unique_numbers = set()

    # Add numbers to the set
    for num in numbers:
        unique_numbers.add(num)

    # Create a new list with unique integers
    cleaned_numbers = [num for num in unique_numbers if num > 0]

    return cleaned_numbers

# Unit tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print("Result:", result)

numbers = [2, 4, 2, 1, 5]
result = remove_duplicates(numbers)
print("Result:", result)

numbers = [2, 2, 2]
result = remove_duplicates(numbers)
print("Result:", result)
```
The code implements a function called **remove_duplicates** that takes a list of integers as input and returns a new list with unique integer values after removing duplicates. The function uses a set to keep track of unique integers and a list comprehension to filter out non-positive numbers. The unit tests demonstrate the expected behavior of the function, which successfully removes duplicates from various input lists.