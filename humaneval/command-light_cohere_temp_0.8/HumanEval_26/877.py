```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize Set to store unique numbers
    unique_numbers = set()
    
    # Add all elements to the set
    for num in numbers:
        unique_numbers.add(num)
    
    # Convert the set to list
    return list(unique_numbers)
``` 
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with all unique integers. The function uses the unique set data structure to keep track of unique numbers and removes duplicates. 

Note: This code uses the set data structure to automatically handle duplicates and provides a more efficient way to solve the problem of removing duplicates from a list of integers.