```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    :param numbers: Space-delimited string of numbers
    :return: Sorted string of numbers
    """
    # Mapping of string representation of numbers to their integer values
    num_dict: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split input string into list of numbers
    num_list: List[str] = numbers.split()

    # Sort list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join sorted list into string and return
    return''.join(sorted_num_list)

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```

In this script, we define a dictionary `num_dict` that maps each string representation of a number to its integer value. We then split the input string into a list of numbers, sort this list based on the integer values of the numbers, and finally join the sorted list back into a string. The sorted string is then returned by the function.