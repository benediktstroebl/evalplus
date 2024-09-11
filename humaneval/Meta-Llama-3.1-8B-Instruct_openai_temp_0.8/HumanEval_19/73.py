```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Parameters:
    numbers (str): A space-delimited string of numbers
    
    Returns:
    str: The input string with numbers sorted from smallest to largest
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Define a dictionary to map string numbers to integer values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_num_list)
    
    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numbers, splits it into a list, maps each number to an integer using a dictionary, sorts the list based on the integer values, and then joins the sorted list back into a string separated by spaces. The function is then tested with the input string `'three one five'`.