```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of space-separated numbers from 0-9 and sorts them in ascending order. The function first converts the input string into a list of integers using `split()` to separate the numbers and `int()` to convert each number. Then, it uses the `sort()` method to sort the numbers in ascending order. Finally, the function returns a string where the numbers are joined back together with spaces between them, resulting in a sorted string of numbers.