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
    
    # Define a dictionary to map number words to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Use a lambda function as the sorting key to convert number words to integers
    # and then sort the list of number words
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers =''.join(sorted_num_list)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a string of space-delimited number words as input, sorts the number words in ascending order, and returns the sorted string. The function uses a dictionary to map number words to their integer values, which are then used as sorting keys. The sorted list of number words is then joined back into a string and returned.