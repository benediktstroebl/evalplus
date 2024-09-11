```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): Space-delimited string of numbers

    Returns:
        str: Sorted string of numbers
    """
    # Create a dictionary to map string numbers to their integer equivalents
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Convert the list of strings to a list of integers
    num_list_int: List[int] = [num_map[num] for num in num_list]

    # Sort the list of integers
    num_list_int.sort()

    # Convert the list of integers back to a list of strings
    num_list_str: List[str] = [list(num_map.keys())[list(num_map.values()).index(i)] for i in num_list_int]

    # Join the list of strings back into a single string
    sorted_str: str =''.join(num_list_str)

    return sorted_str


# Example usage
print(sort_numbers('three one five'))  # 'one three five'
print(sort_numbers('nine eight seven'))  #'seven eight nine'
print(sort_numbers('five four three two one zero'))  # 'one zero two three four five'
```

This script defines a function `sort_numbers` that takes a space-delimited string of numberals, sorts them from smallest to largest, and returns the sorted string. It uses a dictionary to map string numbers to their integer equivalents, and then uses list comprehensions and the built-in `sort` function to sort the integers and convert them back to strings.