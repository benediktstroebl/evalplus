```python
# Define a dictionary that maps number strings to their integer values
number_mapping = {
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
    # Split the input string into a list of numbers
    numbers_list = numbers.split()
    
    # Use the dictionary to get the integer values for each number
    numbers_list = [number_mapping[num] for num in numbers_list]
    
    # Sort the list of numbers
    numbers_list.sort()
    
    # Use the dictionary to get the string values for each number
    sorted_numbers_list = [number_mapping[num] for num in numbers_list]
    
    # Join the sorted list back into a string
    sorted_numbers_string =''.join(sorted_numbers_list)
    
    return sorted_numbers_string

# Test the function
print(sort_numbers('three one five'))  
```

This script first defines a dictionary that maps each number string to its corresponding integer value. The `sort_numbers` function then splits the input string into a list of numbers, uses this dictionary to get their integer values, sorts the list, converts the sorted list back to a list of string numbers, and finally joins this list back into a string.