```python
# Define a dictionary to map string numbers to their integer equivalents
num_dict = {
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
    num_list = numbers.split()
    
    # Use a list comprehension to create a new list with the numbers sorted
    sorted_num_list = sorted([num_dict[num] for num in num_list])
    
    # Use a list comprehension to create a new list with the sorted numbers converted back to strings
    sorted_str_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_num_list]
    
    # Join the sorted list of numbers back into a string
    sorted_str =''.join(sorted_str_list)
    
    return sorted_str

# Example usage:
print(sort_numbers('three one five'))  # Output: 'one three five'
```

This script first defines a dictionary `num_dict` to map string numbers to their integer equivalents. It then defines the `sort_numbers` function, which splits the input string into a list of numbers, sorts this list, and then converts the sorted numbers back into strings before joining them back into a string. The example usage at the end demonstrates how to use this function.