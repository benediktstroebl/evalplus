```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script provides a function that takes a string of numbers and sorts them using Python's built-in sorting function. The function first splits the input string into a list of numbers, then sorts that list, and finally converts the sorted list of numbers back to a string. This solution adheres to the problem statement, as it sorts the numbers from smallest to largest, and is encapsulated within a single function.