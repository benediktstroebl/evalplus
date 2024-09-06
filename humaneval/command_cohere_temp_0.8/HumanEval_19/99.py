```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a sequence of numbers and sorts it in ascending order. The function splits the input string into individual numbers, converts them to integers, sorts the list of integers, and then converts the sorted integers back to strings and joins them together into a single string. The result is a string containing the numbers sorted in ascending order, ready for further processing or display.