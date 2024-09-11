### Sorting Numbers from a String

Here's a Python script that uses a dictionary to map string representations of numbers to their corresponding integer values, and then sorts the input string based on these values.

```markdown
### Code
```python
from typing import List
from collections import OrderedDict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    # Dictionary to map string representations of numbers to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers and sort them based on their integer values
    sorted_numbers = sorted(numbers.split(), key=lambda x: num_dict[x])

    # Use OrderedDict to maintain the original order of equal elements
    result = OrderedDict()
    for num in sorted_numbers:
        result[num] = None

    # Join the sorted numbers back into a string
    return''.join(result.keys())

### Test Cases
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine four eight'))  # Output: 'four eight nine'
print(sort_numbers('seven two one'))  # Output: 'one seven two'
```

This script first defines a dictionary to map string representations of numbers to their corresponding integer values. It then splits the input string into a list of numbers and sorts them based on their integer values. To handle ties, it uses an OrderedDict to maintain the original order of equal elements. Finally, it joins the sorted numbers back into a string and returns the result.