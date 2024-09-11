```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.

    Returns:
        str: The string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map string numbers to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of string numbers
    num_list: List[str] = numbers.split()

    # Sort the list of string numbers based on their corresponding integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list of string numbers back into a string
    sorted_str: str =''.join(num_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four eight six'))  # Output: 'four six eight nine'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers from 'zero' to 'nine' as input, sorts them based on their integer values, and returns the sorted string. The function uses a dictionary to map string numbers to their corresponding integer values, and it leverages the built-in `sort` method to sort the list of string numbers. The sorted list is then joined back into a string using the `join` method.