```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list = numbers.split()
    
    # Use a list comprehension to sort the list of numbers
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four nine'))  # Output: 'four eight nine'
print(sort_numbers('seven five six'))   # Output: 'five six seven'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine', sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map string numbers to their integer values, and then uses the `sorted` function with a lambda function as the `key` argument to sort the list of numbers.