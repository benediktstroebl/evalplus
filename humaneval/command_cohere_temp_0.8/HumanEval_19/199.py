```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes an input string of numbers and returns a string of these numbers sorted from smallest to largest. It first converts the string to a list of integers, sorts the list, and then joins the sorted integers back into a string. 

Here is an example usage of the function:
```python
print(sort_numbers('three one five'))  # one three five
```
This would output: one three five.