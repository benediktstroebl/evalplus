Here's the self-contained Python function that solves the problem:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(x) for x in numbers. String sorting is numbers, so we'll use Python's built-in sort() function to sort them. The sorted numbers will then be converted back into a string by joining them with spaces.

# Run some tests on the function
numbers_list = ['three onefive', '123456', 'abc123', '9', 'abc', '1234567']
sorted_string = sort_numbers(numbers_list)
print(sorted_string)  # Output should be 'three 123456 seven abc123 nine abc six hundred seven hundred'
``` 
This function, named `sort_numbers`, takes a string of numbers as input and returns a string that has the numbers sorted from smallest to largest. The numbers are separated by spaces, and the function works by converting each number to an integer and then sorting them using Python's sort() function.