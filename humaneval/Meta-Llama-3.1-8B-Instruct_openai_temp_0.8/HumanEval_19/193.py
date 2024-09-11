```python
from typing import List, Dict

# Define a dictionary to map string numbers to integer values
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a list comprehension to convert the numbers to integers and sort the list
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string with spaces in between
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))
print(sort_numbers('nine eight seven'))
print(sort_numbers('four five six'))
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers, sorts them in ascending order, and returns the sorted string. The sorting is done based on the corresponding integer values of the numbers, which are stored in a dictionary `num_dict`. The script includes example use cases to demonstrate the function's behavior.