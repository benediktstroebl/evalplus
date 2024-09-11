Here is a Python script that solves the problem:
```python
from typing import List, Dict

# Define a dictionary to map string numbers to integer values
num_dict: Dict[str, int] = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
                           'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use the num_dict to map string numbers to integer values and then sort the list
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five nine seven'))  # Output: 'five seven nine'
```
This script uses a dictionary to map string numbers to integer values, and then uses the `sort()` method to sort the list of numbers based on their integer values. The sorted list is then joined back into a string using the `join()` method.