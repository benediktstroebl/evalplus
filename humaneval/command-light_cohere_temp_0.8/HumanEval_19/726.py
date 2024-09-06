```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = numbers.split()
    string(List(numbers) )
    return string(''.join(sorted(numbers)))

# Tests
numbers_list = ['three', 'one', 'five']
sorted_string = sort_numbers(''.join(numbers_list) )
print(sorted_string) # Output should be: one three five

numbers_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
sorted_string = sort_numbers(''.join(numbers_list) )
print(sorted_string) # Output should be: two three four five six seven eight nine
``` 
The above code defines a function sort_numbers that takes a space-separated string of numbers and returns a string with the numbers sorted from smallest to largest. The tests section passes the
the test cases using the numbers_list variable, and the output is printed to the console.