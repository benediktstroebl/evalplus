```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number words to their integer values
    number_values = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_numbers = sorted(number_list, key=lambda x: number_values[x])

    # Join the sorted list of number words back into a string
    sorted_string =''.join(sorted_numbers)

    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```