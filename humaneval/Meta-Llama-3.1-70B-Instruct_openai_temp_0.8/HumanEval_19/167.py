```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of word numbers from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string of space-delimited word numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.

    Examples:
        >>> sort_numbers('three one five')
        'one three five'
    """

    # Define a dictionary to map word numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of word numbers
    num_list: List[str] = numbers.split()

    # Sort the list of word numbers based on their integer equivalents
    num_list.sort(key=lambda x: num_map[x])

    # Join the sorted list back into a string
    sorted_nums: str =''.join(num_list)

    return sorted_nums

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```