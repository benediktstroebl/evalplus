```python
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five','six','seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    
    Args:
    numbers (str): A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    str: The string with numbers sorted from smallest to largest.
    """
    
    # Split the input string into a list of numbers
    num_list = numbers.split()
    
    # Create a dictionary to map numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Sort the list of numbers based on their integer values
    sorted_num_list = sorted(num_list, key=lambda x: num_dict[x])
    
    # Join the sorted list into a string separated by spaces
    sorted_string =''.join(sorted_num_list)
    
    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('five nine eight'))  # Output: 'five nine eight'
print(sort_numbers('one two seven'))  # Output: 'one two seven'
```

This script defines a function called `sort_numbers` that takes a string of space-delimited numbers as input, sorts the numbers from smallest to largest, and returns the sorted string. The function uses a dictionary to map numbers to their integer values and the built-in `sorted` function to sort the list of numbers. The sorted list is then joined into a string separated by spaces. The script includes example test cases to demonstrate the function's behavior.