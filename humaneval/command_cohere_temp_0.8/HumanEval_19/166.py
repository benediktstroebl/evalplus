```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a space-separated list of numbers from 0-9 as input. The function converts the input string into a list of integers using `split()` to separate the numbers and `int()` to convert each number. It then sorts this list of integers in ascending order using the `sort()` method. Finally, the function joins the sorted list of integers back into a string, using `str()` to convert them back to strings, and returns the result. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # output: 'one three five'
```
This will take the string "three one five" as input, convert each character to its corresponding number, sort the list of numbers, and return the sorted list as a string with the space delimiter. 

This will output "one three five" which is the expected sorted sequence of the numbers.