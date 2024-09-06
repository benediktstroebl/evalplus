```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes as input a string of numbers from 0-9 inclusive, each printed separately. The function first splits the input string into individual numbers, then sorts these numbers numerically before converting them back to a string and returning the result. This fulfills the prompt's requirement of sorting the numbers from smallest to largest.