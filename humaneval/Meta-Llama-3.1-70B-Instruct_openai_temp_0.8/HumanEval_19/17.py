```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A string containing space-delimited numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary that maps numberals to their integer values
    numeral_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numberals
    num_list: List[str] = numbers.split()
    
    # Sort the list of numberals based on their integer values
    num_list.sort(key=lambda x: numeral_map[x])
    
    # Join the sorted list of numberals back into a string
    sorted_numbers =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```