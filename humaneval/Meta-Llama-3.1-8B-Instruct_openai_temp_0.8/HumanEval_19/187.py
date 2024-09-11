```python
# Define a dictionary to map string numbers to their integer equivalents
number_dict = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
}

def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers (str): A space-delimited string of numbers.

    Returns:
    str: The sorted string of numbers.
    """
    
    # Split the input string into a list of numbers
    num_list = numbers.split()
    
    # Use a list comprehension to sort the list of numbers
    # The sorted function uses the values from the number_dict as the comparison keys
    sorted_list = sorted(num_list, key=lambda x: number_dict[x])
    
    # Join the sorted list back into a string with spaces in between
    sorted_string =''.join(sorted_list)
    
    return sorted_string

# Example usage:
print(sort_numbers('three one five'))  # Output: one three five
print(sort_numbers('nine five four'))  # Output: four five nine
```

This script first defines a dictionary that maps string numbers to their integer equivalents. The `sort_numbers` function splits the input string into a list of numbers, sorts this list using the dictionary values as comparison keys, and then joins the sorted list back into a string. The function returns this sorted string.