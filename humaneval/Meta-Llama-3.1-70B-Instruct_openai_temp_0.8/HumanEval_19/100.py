```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of number words from 'zero' to 'nine' in ascending order.

    Args:
        numbers (str): A string containing space-delimited number words.

    Returns:
        str: A string with the number words sorted from smallest to largest.
    """
    
    # Define a dictionary to map number words to their corresponding integer values
    number_mapping: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into a list of number words
    number_words: List[str] = numbers.split()
    
    # Sort the list of number words based on their corresponding integer values
    sorted_number_words: List[str] = sorted(number_words, key=lambda x: number_mapping[x])
    
    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_number_words)
    
    return sorted_numbers

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```