Here is the Python script that solves the problem:
```python
from typing import Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    # Create a dictionary to map numerals to their integer equivalents
    numeral_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of numerals
    numerals: List[str] = numbers.split()
    
    # Use a lambda function as the key for the sorted function
    sorted_numerals: List[str] = sorted(numerals, key=lambda x: numeral_map[x])
    
    # Join the sorted numerals back into a string
    result: str =''.join(sorted_numerals)
    
    return result

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
```