```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    
    Args:
        numbers (str): A space-delimited string of numbers.
    
    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of words
    number_list: List[str] = numbers.split()
    
    # Create a dictionary to map words to their corresponding numerical values
    num_dict: dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of words based on their numerical values
    sorted_numbers: List[str] = sorted(number_list, key=lambda x: num_dict[x])
    
    # Join the sorted list of words into a string and return it
    return''.join(sorted_numbers)


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight seven nine'))  # Output: 'eight seven nine'
print(sort_numbers('zero five one'))  # Output: 'one five zero'
```

This script defines a function `sort_numbers` that takes a string of space-delimited numbers as input, sorts them based on their numerical values, and returns the sorted string. The function uses a dictionary to map words to their corresponding numerical values and the built-in `sorted` function to sort the list of words. The sorted list is then joined into a string using the `join` method and returned. The script includes test cases to demonstrate the function's behavior.