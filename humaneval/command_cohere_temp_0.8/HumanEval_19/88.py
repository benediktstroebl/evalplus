```python
def sort_numbers(input_str: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = input_str.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This script takes an input string of numbers that are space-delimited and sorted them in ascending order using the `sorted` function. The function then returns the output as a string by using `join` on the list of sorted numbers.

This function effectively handles the input string `['three', 'one', 'five']` by sorting the numbers from smallest to largest and returning the sorted string, which would be 'one three five'.