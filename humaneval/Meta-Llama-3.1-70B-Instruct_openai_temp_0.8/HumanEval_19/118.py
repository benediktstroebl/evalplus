```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Create a dictionary to map numberals to their integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
       'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()
    
    # Sort the list based on the integer values of the numberals
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list into a string and return it
    return''.join(sorted_num_list)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first creating a dictionary that maps each numeral to its corresponding integer value. It then splits the input string into a list of numberals, sorts the list based on the integer values of the numberals, and finally joins the sorted list into a string and returns it. The `key` argument of the `sorted` function is a lambda function that looks up the integer value of each numeral in the dictionary.