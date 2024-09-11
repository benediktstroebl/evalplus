```python
from typing import List, Dict


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    :param numbers: A string of numbers separated by spaces
    :return: A string of numbers sorted from smallest to largest, separated by spaces
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Create a dictionary to map the words to their corresponding integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list into a string, separated by spaces
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))
```

This script defines a function `sort_numbers` that takes a string of numbers separated by spaces, maps the words to their corresponding integer values, sorts the numbers based on the integer values, and returns the sorted string. The test at the end checks that the function works correctly for the example input.