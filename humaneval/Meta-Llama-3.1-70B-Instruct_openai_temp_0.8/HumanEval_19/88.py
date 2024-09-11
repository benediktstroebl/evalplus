```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' 
    in ascending order.

    Args:
        numbers: A space-delimited string of numberals.

    Returns:
        A string with numbers sorted from smallest to largest.

    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script works by first defining a dictionary that maps number words to their integer values. It then splits the input string into a list of number words, sorts the list based on the integer values, and finally joins the sorted list back into a string. The `key` argument of the `sort` method is a function that takes a number word as input and returns its integer value. The `lambda` function is used to define this function inline.