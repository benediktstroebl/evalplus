```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Create a dictionary to map the numberals to their corresponding integer values
    number_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numberals
    numeral_list: List[str] = numbers.split()
    
    # Validate the input
    for numeral in numeral_list:
        if numeral not in number_map:
            raise ValueError(f"Invalid numeral: {numeral}")
    
    # Sort the list of numberals based on their corresponding integer values
    sorted_numerals = sorted(numeral_list, key=lambda x: number_map[x])
    
    # Join the sorted list of numberals back into a string
    sorted_numbers =''.join(sorted_numerals)
    
    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```