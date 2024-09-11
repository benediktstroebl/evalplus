```python
def sort_numbers(numbers: str) -> str:
    """
    Sorts a space-delimited string of numbers from 'zero' to 'nine' in ascending order.

    Args:
    numbers: A space-delimited string of numbers from 'zero' to 'nine'.

    Returns:
    A string with numbers sorted from smallest to largest.

    Example:
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define a dictionary to map string numbers to their integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5,'six': 6,'seven': 7, 'eight': 8, 'nine': 9
    }

    # Split the input string into a list of string numbers
    num_list = numbers.split()

    # Sort the list of string numbers based on their integer values
    num_list.sort(key=lambda x: num_dict[x])

    # Join the sorted list of string numbers into a single string
    sorted_string =''.join(num_list)

    return sorted_string

# Test the function
print(sort_numbers('three one five'))  # Output: 'one three five'
print(sort_numbers('nine eight seven six five four three two one'))  # Output: 'one two three four five six seven eight nine'
```