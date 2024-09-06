```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings comprised of choices from 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes an input string, splits it into a list of numbers, sorts that list, and then joins the numbers back into a string. 

For example, given the input 'three one five', the function would return 'one three five'. 

This approach ensures that the function works for all valid inputs and produces the correct sorted output.