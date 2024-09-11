```python
from typing import Dict

# Define a dictionary to map string representations of numbers to their integer values
num_map: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers from 'zero' to 'nine'

    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    numbers_list: List[str] = numbers.split()

    # Use a list comprehension to sort the numbers based on their integer values
    sorted_list: List[str] = sorted(numbers_list, key=lambda x: num_map[x])

    # Join the sorted list into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine nine five'))
print(sort_numbers('zero two five nine'))
```
This script uses a dictionary to map string representations of numbers to their integer values. It then splits the input string into a list of numbers, sorts the list based on the integer values, and joins the sorted list into a string separated by spaces. The function is tested with a few examples.