Here's how you can solve this problem using Python:

```python
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerical words from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Create a dictionary mapping number words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    num_list: List[str] = numbers.split()

    # Use a lambda function with the sorted function to sort the list of number words based on their integer values
    sorted_list: List[str] = sorted(num_list, key=lambda x: num_dict[x])

    # Join the sorted list of number words back into a string separated by spaces
    sorted_string: str =''.join(sorted_list)

    return sorted_string


# Test the function with the provided example
print(sort_numbers('three one five'))
```

This script sorts a space-delimited string of numerical words from 'zero' to 'nine' in ascending order by their integer values. It uses a dictionary to map the number words to their corresponding integer values, and then sorts the list of number words based on these integer values. Finally, it joins the sorted list back into a string separated by spaces.