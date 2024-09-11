```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()
    
    # Sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of number words back into a string
    sorted_string: str =''.join(sorted_list)
    
    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of number words as input, sorts them in ascending order based on their integer values, and returns the sorted string. The function uses a dictionary to map number words to their integer values and the built-in `sorted` function to sort the list of number words. The sorted list is then joined back into a string and returned as the result.