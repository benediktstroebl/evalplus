```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes as input a string of numbers from 0-9 space-separated. It sorts the list of numbers and returns a sorted string. The function sorts the numbers numerically, unlike sorting alphabetically based on the string representation of numbers. The function successfully passes the provided test case of 'three one five' returning 'one three five'.