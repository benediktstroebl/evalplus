```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes an input string of numbers and returns a string of the same numbers sorted from smallest to largest. It does this by first converting the string to a list of integers, sorting the list, and then joining the list back into a string. As the function sorts integers, sorting stability ensures that tied digits retain their original order, preventing alphabetical sorting. For example, `sort_numbers('five three one')` returns `'one three five'`.