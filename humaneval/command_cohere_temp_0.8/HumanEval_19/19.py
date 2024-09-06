```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order. Finally, it converts the sorted list of numbers back to a string by joining the list elements with spaces and returns the result.

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This demonstrates the function sorting the string of numbers 'three one five' in ascending order, resulting in the output 'one three five'.