```python
from typing import List, Dict

def sort_numbers(numbers_str: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers_str (str): A space-delimited string of numberals.

    Returns:
        str: A string with numbers sorted from smallest to largest.
    """
    # Create a dictionary mapping number words to their integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    numbers_list: List[str] = numbers_str.split()

    # Sort the list of number words based on their integer values
    sorted_numbers_list: List[str] = sorted(numbers_list, key=lambda x: number_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers_str: str =''.join(sorted_numbers_list)

    return sorted_numbers_str


# Example usage:
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```