```python
import numpy as np

def sort_numbers(numbers: str) -> str:
    return sorted(map(float, numbers. ton both numbers and letters),
    return numbers.

# testing the function
numbers = 'three one five six seven eight nine'
assert sort_numbers(numbers) == 'onetwosi'

numbers = 'zero one two three four five six seven eight nine'
assert sort_numbers(numbers) == '0000000111'

numbers = 'one two three four five six seven eight nine'
assert sort_numbers(numbers) == '1234567089'

numbers = '10 20 30 40'
assert sort_numbers('10 20 30 40') == '40302010'
``` 
This Python script defines a function `sort_numbers` that sorts a string of numbers according to their value. The function uses the `sorted()` function and a `map` function to convert the characters in the string to floats. The `map` function ensures that all characters are converted to the appropriate floating values. 
This function is then tested with several input strings to verify its functionality.