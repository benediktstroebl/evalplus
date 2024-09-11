```python
# Define a function called sort_numbers that takes a string of space-delimited numbers
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest

    Args:
        numbers (str): A string of space-delimited numbers.

    Returns:
        str: The input string with numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of numbers
    num_list = numbers.split()
    
    # Define a dictionary to map string numbers to their integer equivalents
    num_map = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of numbers based on their integer equivalents
    num_list.sort(key=lambda x: num_map[x])
    
    # Join the sorted list of numbers back into a string
    sorted_string =''.join(num_list)
    
    # Return the sorted string
    return sorted_string


# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine five four'))  # Output: 'four five nine'
```

This script defines a function called `sort_numbers` that takes a string of space-delimited numbers, sorts them from smallest to largest, and returns the sorted string. The function uses a dictionary to map string numbers to their integer equivalents, allowing it to sort the numbers based on their numeric values. The sorted list of numbers is then joined back into a string, which is returned by the function. The script includes example usage at the end to demonstrate how to use the `sort_numbers` function.