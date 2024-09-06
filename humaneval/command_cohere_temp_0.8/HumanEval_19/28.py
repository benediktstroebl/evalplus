```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order using the `sort()` method and converts the sorted list of integers back into a string. 

The function sorts the numbers regardless of their position in the string and returns the sorted string without any rearrangement of the characters.