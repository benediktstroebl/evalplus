```python
from typing import List, Dict

def sort_numbers(numbers: str) -> str:
    """
    Inputs a space-delimited string of numberals from 'zero' to 'nine' and returns 
    the string with numbers sorted from smallest to largest.
    
    Args:
    numbers (str): A space-delimited string of numberals from 'zero' to 'nine'.
    
    Returns:
    str: The input string with numbers sorted from smallest to largest.
    """

    # Define a dictionary that maps number words to their integer values
    number_map: Dict[str, int] = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of number words
    number_list: List[str] = numbers.split()

    # Sort the list of number words based on their integer values
    sorted_number_list: List[str] = sorted(number_list, key=lambda x: number_map[x])

    # Join the sorted list of number words back into a string
    sorted_numbers: str =''.join(sorted_number_list)

    return sorted_numbers


# Example usage
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```