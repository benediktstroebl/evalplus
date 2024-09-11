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
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of words
    num_list: List[str] = numbers.split()
    
    # Sort the list based on the corresponding numerical values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```
This script works by first creating a dictionary that maps the word representations of numbers to their numerical values. It then splits the input string into a list of words, sorts this list based on the corresponding numerical values, and finally joins the sorted list back into a string.