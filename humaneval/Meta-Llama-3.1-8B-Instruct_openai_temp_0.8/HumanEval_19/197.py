```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers

    Returns:
        str: The sorted string of numbers
    """
    # Create a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers back into a string
    sorted_numbers =''.join(sorted_num_list)

    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('eight nine seven'))  # Output: seven eight nine
```

In this script, we define a function `sort_numbers` that takes a space-delimited string of numbers as input, sorts the numbers in ascending order based on their integer values, and returns the sorted string. We use a dictionary to map the string numbers to their integer values for efficient sorting. The function is then tested with some example inputs.