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

This script takes an input string of numbers that are space-delimited and sorted them using the `sorted` function. It then joins the numbers back into a string for the correct output format. 

Here are some example inputs and outputs to test the function:
```python
input = 'zero nine eight seven six five four three two one'
assert sort_numbers(input) == 'zero one two three four five six seven eight nine'

input = 'nine eight seven six five four three two one zero'
assert sort_numbers(input) == 'zero one two three four five six seven eight nine'

input = 'one two three four five six seven eight nine'
assert sort_numbers(input) == 'one two three four five six seven eight nine'
```