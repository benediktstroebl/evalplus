```python
def sort_numbers(input_string: str) -> str:
    """
    Sorts a space-delimited string of numbers from smallest to largest.
    Valid inputs are strings containing digits 'zero' to 'nine'.
    Returns the sorted string.
    """
    numbers = input_string.split()
    sorted_numbers = ' '.join(sorted(numbers))
    return sorted_numbers
```

This function takes in a string variable containing space-delimited numbers from 'zero' to 'nine' and sorts the numbers from smallest to largest. It then returns the sorted string. 

To ensure accuracy, test your function under different scenarios using test cases like the ones provided in the Markdown code block. Feel free to adapt these test cases to any specific requirements or edge cases that might apply to your function.