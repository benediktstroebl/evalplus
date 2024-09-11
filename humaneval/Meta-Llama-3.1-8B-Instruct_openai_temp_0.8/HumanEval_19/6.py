```python
from typing import Dict

# Mapping of number strings to integers for easy comparison
number_mapping: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number strings from 'zero' to 'nine'.

    Args:
    numbers (str): A space-delimited string of number strings.

    Returns:
    str: The sorted string with numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_mapping[x])
    
    # Join the sorted list back into a string
    sorted_numbers: str =''.join(num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first defines a dictionary `number_mapping` to map the number strings to integers. The `sort_numbers` function then splits the input string into a list, sorts this list based on the integer values of the numbers, and finally joins the sorted list back into a string.