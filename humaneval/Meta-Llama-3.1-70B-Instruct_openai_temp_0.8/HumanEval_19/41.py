```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    This function takes a string of space-delimited numerals from 'zero' to 'nine',
    and returns the string with numbers sorted from smallest to largest.

    Args:
    numbers (str): A string of space-delimited numerals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map numeral strings to their integer values
    num_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numeral strings
    num_list: List[str] = numbers.split()

    # Sort the list of numeral strings based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list of numeral strings back into a single string
    sorted_str: str =''.join(sorted_list)

    return sorted_str


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one zero'))  # Output: 'zero one two three four five six seven eight nine'
```