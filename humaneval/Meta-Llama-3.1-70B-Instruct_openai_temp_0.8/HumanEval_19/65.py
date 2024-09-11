```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    
    # Define a dictionary to map word numbers to their integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of word numbers
    word_numbers: List[str] = numbers.split()
    
    # Sort the word numbers based on their integer values
    sorted_word_numbers: List[str] = sorted(word_numbers, key=lambda x: number_map[x])
    
    # Join the sorted word numbers back into a string separated by spaces
    sorted_numbers: str =''.join(sorted_word_numbers)
    
    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'
```