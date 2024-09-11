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
    
    # Create a dictionary to map numeral strings to integer values
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numeral strings
    numeral_list: List[str] = numbers.split()
    
    # Sort the list of numeral strings based on their corresponding integer values
    sorted_numerals: List[str] = sorted(numeral_list, key=lambda x: numeral_map[x])
    
    # Join the sorted list of numeral strings into a single string
    sorted_string: str =''.join(sorted_numerals)
    
    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```