```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """

    # Create a dictionary to map word numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split input string into a list of words
    num_list = numbers.split()

    # Sort the list based on the integer values of the words
    sorted_list = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers =''.join(sorted_list)

    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```

To test this code, save it in a Python file, e.g., `sort_numbers.py`, and run it using Python, e.g., `python sort_numbers.py`. You can also modify the input string to test different scenarios.