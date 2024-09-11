```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Parameters:
    numbers (str): A space-delimited string of numbers
    
    Returns:
    str: The sorted string of numbers
    """
    
    # Define a dictionary to map numbers to their numerical values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their numerical values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(sorted_num_list)
    
    return sorted_numbers

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('four nine seven'))  # Output: 'four seven nine'
print(sort_numbers('eight five three'))  # Output: 'three five eight'
```

This Python script defines a function `sort_numbers` that takes a space-delimited string of numbers as input, maps each number to its numerical value, sorts the list of numbers based on their numerical values, and returns the sorted string of numbers. The function uses a dictionary to map numbers to their numerical values and the built-in `sorted` function with a custom sorting key to sort the list of numbers.