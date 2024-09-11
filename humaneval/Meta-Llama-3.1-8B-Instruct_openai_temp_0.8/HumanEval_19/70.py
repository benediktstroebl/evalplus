```python
from typing import List, Dict

# Dictionary to map string numbers to integers
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

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
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Convert the list of strings to a list of integers using the num_dict
    num_list: List[int] = [num_dict[num] for num in num_list]

    # Sort the list of integers
    num_list.sort()

    # Convert the list of integers back to a list of strings using the num_dict
    sorted_num_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(i)] for i in num_list]

    # Join the sorted list of strings into a single string
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six'))  # Output:'six seven eight nine'
```

This script uses a dictionary `num_dict` to map string numbers to integers. The `sort_numbers` function splits the input string into a list of numbers, converts the list of strings to a list of integers, sorts the list of integers, and then converts the list of integers back to a list of strings using the `num_dict`. Finally, the function joins the sorted list of strings into a single string.