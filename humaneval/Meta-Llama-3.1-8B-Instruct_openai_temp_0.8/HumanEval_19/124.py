```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map string numbers to their integer equivalents
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer equivalents
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_map[x])
    
    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine', sorts them in ascending order, and returns the sorted string. It uses a dictionary to map string numbers to their integer equivalents for sorting purposes. The function is tested with the example input 'three one five'.