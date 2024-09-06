```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set()

    # Add numbers to the set
    for num in numbers:
        unique_numbers.add(num)

    # Create a new list with unique numbers
    cleaned_numbers = [num for num in unique_numbers if num != None]

    return cleaned_numbers
``` 
The code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate numbers removed. The function utilizes the's the concept of a set to store unique integers and creates a new list with the unique elements from the original input list.