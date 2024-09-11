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
    
    # Create a dictionary to map word numbers to their digital equivalents
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of word numbers
    num_list = numbers.split()
    
    # Sort the list based on the digital equivalents of the word numbers
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list back into a string
    sorted_string =''.join(sorted_list)
    
    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight four two'))  # Output: 'two four eight'
```

This script works by first creating a dictionary to map word numbers to their digital equivalents. It then splits the input string into a list of word numbers and sorts this list based on the digital equivalents of the word numbers. Finally, it joins the sorted list back into a string and returns the result.