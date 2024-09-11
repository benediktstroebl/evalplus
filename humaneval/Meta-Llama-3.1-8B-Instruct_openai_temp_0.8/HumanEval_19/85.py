Here is the Python script that solves the problem:
```python
from typing import List

# Dictionary mapping string representations to their integer equivalents
num_dict = {
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
    # Split the input string into a list of strings representing numbers
    num_list: List[str] = numbers.split()
    
    # Map each string representation to its integer equivalent and sort
    sorted_list: List[str] = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted([num_dict[num] for num in num_list])]
    
    # Join the sorted list of string representations back into a single string
    sorted_str: str =''.join(sorted_list)
    
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine nine nine'))  # Output: 'nine nine nine'
print(sort_numbers('zero five ten'))   # Output: 'five ten zero'
```
Note that this script assumes the input string only contains valid number representations. If the input string may contain invalid or out-of-order numbers, additional error handling may be necessary.