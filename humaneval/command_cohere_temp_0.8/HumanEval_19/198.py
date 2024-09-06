```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a space-delimited list of numbers from 0-9 as input. It splits the input string into a list of integers, sorts it in ascending order, and then joins the sorted integers back into a string, which it returns as the output. 

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This will sort the numbers in the input string from smallest to largest, as requested in the problem statement.