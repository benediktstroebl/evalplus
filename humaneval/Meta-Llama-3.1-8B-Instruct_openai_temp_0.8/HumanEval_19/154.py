```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Create a dictionary to map string numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of string numbers
    num_list: list[str] = numbers.split()
    
    # Sort the list of string numbers based on their integer values
    sorted_list: list[str] = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string separated by spaces
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str


# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight nine zero'))  # Output: 'zero eight nine'
print(sort_numbers('five five one'))  # Output: 'one five five'
```

This script will correctly sort the input string of numbers and return the sorted string. It uses a dictionary to map the string numbers to their corresponding integer values, allowing it to sort the numbers based on their values.