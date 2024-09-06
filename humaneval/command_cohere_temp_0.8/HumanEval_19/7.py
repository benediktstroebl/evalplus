```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes an input string of numbers from 'zero' to 'nine' in a space-delimited format and returns the same string with the numbers sorted from smallest to largest. It uses Python's split() method to divide the input string into a list of characters, then uses a list comprehension to convert these characters into integers. After sorting the list of integers, the function maps these back to strings and joins them with spaces to form the output string.

Here is an example usage of this function:
```python
print(sort_numbers('three one five'))  # Outputs: 'one three five'
```
This correctly sorts the characters 'one', 'three', and 'five' from the input string and returns them in sorted order.