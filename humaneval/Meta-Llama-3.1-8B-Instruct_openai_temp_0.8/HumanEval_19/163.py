```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers (zero to nine) in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
    str: The sorted string with numbers.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Define a dictionary to map number names to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    sorted_numbers: List[str] = sorted(numbers_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string
    sorted_string: str =''.join(sorted_numbers)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output: 'eight seven nine'
print(sort_numbers('zero five two'))  # Output: 'two five zero'
```

This Python script defines a function `sort_numbers` that sorts a space-delimited string of numbers (zero to nine) in ascending order. It uses a dictionary to map number names to their integer values, and the built-in `sorted` function to sort the list of numbers. The function then joins the sorted list of numbers back into a string and returns it.