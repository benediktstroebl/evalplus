```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    This function takes a space-delimited string of numberals from 'zero' to 'nine', 
    and returns the string with numbers sorted from smallest to largest.

    Args:
        numbers (str): A space-delimited string of numberals.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """

    # Define a dictionary to map number words to their corresponding integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Sort the list of number words based on their corresponding integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_map[x])

    # Join the sorted list into a string and return
    return''.join(sorted_num_list)


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```