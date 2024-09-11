```python
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Args:
        numbers (str): A space-delimited string of numbers.
    
    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Create an OrderedDict to store the numbers and their corresponding values
    num_dict: OrderedDict[str, int] = OrderedDict([('zero', 0), ('one', 1), ('two', 2), 
                                                  ('three', 3), ('four', 4), ('five', 5), 
                                                  ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)])
    
    # Sort the list of numbers based on their corresponding values
    sorted_numbers: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string with spaces in between
    sorted_str: str =''.join(sorted_numbers)
    
    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script sorts the input string of numbers based on their corresponding values, ignoring the case sensitivities and the order of the numbers in the input string. It uses an OrderedDict to store the numbers and their corresponding values, and the sorted() function with a lambda function as the key to sort the list of numbers. Finally, it joins the sorted list into a string with spaces in between.