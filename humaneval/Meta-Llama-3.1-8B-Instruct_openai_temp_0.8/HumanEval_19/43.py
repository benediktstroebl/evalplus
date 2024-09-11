### Sorting Numbers in a String
#### Problem Statement
The `sort_numbers` function takes a space-delimited string of numbers (from 'zero' to 'nine') as input and returns the string with numbers sorted from smallest to largest.

#### Solution
```python
from typing import List

# Mapping of number names to their integer values
NUMBERS = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of numbers
    num_list: List[str] = numbers.split()
    
    # Create a list of tuples where each tuple contains a number and its value
    num_values: List[tuple] = [(num, NUMBERS[num]) for num in num_list]
    
    # Sort the list of tuples based on the number values
    sorted_num_values: List[tuple] = sorted(num_values, key=lambda x: x[1])
    
    # Extract the sorted numbers from the list of tuples
    sorted_num_list: List[str] = [num[0] for num in sorted_num_values]
    
    # Join the sorted list of numbers into a string separated by spaces
    sorted_string: str =''.join(sorted_num_list)
    
    return sorted_string
```

#### Example Use Cases
```python
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight four'))  # Output: 'four eight nine'
print(sort_numbers('zero five two'))  # Output: 'two five zero'
```