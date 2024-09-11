```python
from typing import List, Dict

# Define a dictionary to map string numbers to integer values for comparison
number_map: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): Space-delimited string of numbers

    Returns:
        str: Sorted string of numbers

    Example:
        >>> sort_numbers('three one five')
        'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Use the sorted function with a custom key to sort the list
    sorted_list: List[str] = sorted(num_list, key=lambda x: number_map[x])

    # Join the sorted list back into a string separated by spaces
    sorted_str: str =''.join(sorted_list)

    return sorted_str

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('eight nine seven'))  # Output:'seven eight nine'
print(sort_numbers('five five five'))  # Output: 'five five five'
```
This script defines a dictionary `number_map` to map string numbers to integer values for comparison. The `sort_numbers` function splits the input string into a list of numbers, sorts the list using the `sorted` function with a custom key, and then joins the sorted list back into a string separated by spaces. Finally, it tests the function with several examples.