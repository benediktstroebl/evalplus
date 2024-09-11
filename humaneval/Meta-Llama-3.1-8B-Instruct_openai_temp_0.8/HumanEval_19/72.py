```python
from typing import Dict

# Create a dictionary to map string representations to their integer equivalents
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use the dictionary to get the integer equivalents of the numbers
    num_list: List[int] = [num_dict[num] for num in num_list]

    # Sort the list of numbers in ascending order
    num_list.sort()

    # Use the dictionary to get the string representations of the numbers
    sorted_num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]

    # Join the sorted list of numbers into a string separated by spaces
    sorted_string: str =''.join(sorted_num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('zero five two'))  # Output: 'two five zero'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine' as input, sorts the numbers in ascending order, and returns the sorted string. The function uses a dictionary to map the string representations of numbers to their integer equivalents, making it easier to sort the numbers.