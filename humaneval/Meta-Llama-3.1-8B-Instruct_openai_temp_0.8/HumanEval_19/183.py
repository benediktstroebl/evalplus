```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
    numbers (str): A space-delimited string of numbers

    Returns:
    str: The string with numbers sorted from smallest to largest
    """
    # Define a dictionary to map string numbers to their integer equivalents
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use a list comprehension to map each number to its integer equivalent
    num_list: List[int] = [num_map[num] for num in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Use a list comprehension to map each number back to its string equivalent
    num_list: List[str] = [list(num_map.keys())[list(num_map.values()).index(num)] for num in num_list]

    # Join the sorted list of numbers back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```