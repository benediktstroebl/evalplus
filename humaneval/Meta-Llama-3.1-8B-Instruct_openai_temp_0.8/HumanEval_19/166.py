### Sorting Numbers in a String

Here's a Python script that solves the given problem:
```markdown
### Code
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A space-delimited string of numbers.

    Returns:
        str: The string with numbers sorted from smallest to largest.
    """
    # Define a dictionary to map number names to their integer values
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()

    # Create a list of tuples, where each tuple contains a number name and its value
    num_tuple_list: List[tuple[str, int]] = [(num, num_map[num]) for num in num_list]

    # Sort the list of tuples based on the number values
    num_tuple_list.sort(key=lambda x: x[1])

    # Extract the sorted number names from the list of tuples
    sorted_num_list: List[str] = [num[0] for num in num_tuple_list]

    # Join the sorted number names into a string separated by spaces
    sorted_numbers: str =''.join(sorted_num_list)

    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

### Explanation

This script uses the following steps to solve the problem:

1.  Define a dictionary to map number names to their integer values.
2.  Split the input string into a list of numbers.
3.  Create a list of tuples, where each tuple contains a number name and its value.
4.  Sort the list of tuples based on the number values.
5.  Extract the sorted number names from the list of tuples.
6.  Join the sorted number names into a string separated by spaces.

The script demonstrates the use of a lambda function to extract the number values from the list of tuples during sorting. This allows for efficient and concise sorting based on the number values.