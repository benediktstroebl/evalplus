```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    This function takes a string of space-delimited numberals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Create a dictionary to map numberals to their integer equivalents
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()
    
    # Sort the list of numberals based on their integer equivalents
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])
    
    # Join the sorted list of numberals back into a string
    sorted_numbers: str =''.join(sorted_numerals)
    
    return sorted_numbers


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```