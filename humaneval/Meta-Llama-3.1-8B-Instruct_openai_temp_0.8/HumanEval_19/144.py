Here is a Python script that solves the problem:

```python
# Problem: Sort a string of space-delimited numbers from 'zero' to 'nine' in ascending order.

from typing import Dict

# Define a dictionary to map string representations of numbers to their integer values.
num_dict: Dict[str, int] = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    :param numbers: A space-delimited string of numbers
    :return: The sorted string
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Sort the list of numbers based on their integer values
    sorted_num_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of numbers back into a string with spaces in between
    result: str =''.join(sorted_num_list)

    return result

# Test the function
print(sort_numbers('three one five'))  # Expected output: 'one three five'
print(sort_numbers('nine eight seven'))  # Expected output:'seven eight nine'
print(sort_numbers('five four three two'))  # Expected output: 'two three four five'
```

This script first defines a dictionary `num_dict` to map string representations of numbers to their integer values. It then uses the `sorted` function to sort the input string into a list based on the integer values of the numbers. The sorted list is then joined back into a string with spaces in between, and returned as the result.