```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    
    # Define a dictionary to map string representations to integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])
    
    # Join the sorted list into a string and return it
    return''.join(num_list)

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
print(sort_numbers('zero one two'))  # Output: 'zero one two'
```

This script first defines a dictionary `num_dict` to map string representations of numbers to their integer values. It then splits the input string into a list of numbers and sorts this list based on the integer values of the numbers. Finally, it joins the sorted list into a string and returns it. The test cases demonstrate the function's correctness for different input strings.