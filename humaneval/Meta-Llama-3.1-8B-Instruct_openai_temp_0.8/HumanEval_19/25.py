### Number Sorter Script
```python
# Define a dictionary to map string numbers to their integer equivalents
number_map = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input string into a list of strings
    numbers_list = numbers.split()
    
    # Create a list of tuples where each tuple contains the string and its integer equivalent
    numbers_list = [(num, number_map[num]) for num in numbers_list]
    
    # Sort the list of tuples based on the integer equivalents
    numbers_list.sort(key=lambda x: x[1])
    
    # Return the sorted list of strings joined back into a single string
    return''.join([num for num, _ in numbers_list])

# Example usage:
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('nine five seven'))  # Output: five nine seven
```
This script defines a dictionary to map string numbers to their integer equivalents. It then splits the input string into a list of strings, creates a list of tuples where each tuple contains the string and its integer equivalent, sorts the list of tuples based on the integer equivalents, and finally returns the sorted list of strings joined back into a single string.