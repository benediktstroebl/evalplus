```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid choices are from 'zero' to 'nine'.
    """
    # Split the input string into a list of strings
    numbers = input_string.split()
    
    # Sort the list of strings
    sorted_numbers = sorted(numbers)
    
    # Join the sorted list of strings back into a single string
    sorted_string = ' '.join(sorted_numbers)
    
    return sorted_string
```