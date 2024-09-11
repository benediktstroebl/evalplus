### Sorting Numbers in a String

Here's a Python script that solves the problem. The `sort_numbers` function uses a dictionary to map string representations of numbers to integers, sorts the numbers, and then joins them back into a string.

```markdown
### Code
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine'.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The string with numbers sorted from smallest to largest.

    Examples:
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map string representations of numbers to integers
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into numbers and sort them
    sorted_numbers = sorted(numbers.split(), key=lambda x: num_map[x])

    # Join the sorted numbers back into a string separated by spaces
    sorted_string =''.join(sorted_numbers)

    return sorted_string

### Example Usage
if __name__ == "__main__":
    print(sort_numbers('three one five'))  # Output: 'one three five'
    print(sort_numbers('nine eight seven'))  # Output:'seven eight nine'
    print(sort_numbers('zero five four'))  # Output: 'four five zero'
```

This script defines the `sort_numbers` function, which takes a space-delimited string of numbers as input and returns the string with numbers sorted from smallest to largest. The function uses a dictionary to map string representations of numbers to integers, allowing the numbers to be compared and sorted correctly. The script also includes example usage of the `sort_numbers` function in the `if __name__ == "__main__":` block.