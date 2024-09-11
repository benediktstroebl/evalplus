```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()
    
    # Define a dictionary to map number names to their integer values
    number_map: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of numbers based on their integer values
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: number_map[x])
    
    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_numbers)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five one'))   # Output: 'one five nine'
print(sort_numbers('seven eight nine'))  # Output:'seven eight nine'
```

This Python script first splits the input string into a list of numbers using the `split` method. It then defines a dictionary to map number names to their integer values. The list of numbers is sorted based on their integer values using the `sorted` function and a lambda function as the sorting key. Finally, the sorted list is joined into a string separated by spaces using the `join` method.