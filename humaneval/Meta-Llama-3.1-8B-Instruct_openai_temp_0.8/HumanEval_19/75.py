### Sorting Numbers in a String
#### Problem Statement
Input is a space-delimited string of numbers from 'zero' to 'nine'. 
Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'. 
Return the string with numbers sorted from smallest to largest.

#### Solution

```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numberals from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numberals.

    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a dictionary mapping number names to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Sort the list of numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list back into a string
    sorted_numbers: str =''.join(num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first splits the input string into a list of numbers. It then creates a dictionary mapping each number name to its integer value. The list is sorted based on these integer values, and finally, the sorted list is joined back into a string and returned.