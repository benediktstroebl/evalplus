```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numberals

    Returns:
    str: The string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map string numbers to their integer values
    number_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: number_dict[x])

    # Join the sorted list of numbers back into a string
    sorted_str: str =''.join(num_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five two'))   # Output: 'two five nine'
```

This script first defines a dictionary to map string numbers to their integer values. It then splits the input string into a list of numbers, sorts this list based on the integer values of the numbers, and finally joins the sorted list back into a string. The sorted string is then returned.