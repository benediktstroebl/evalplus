```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This script takes as input a string of numbers from 0-9 and spaces that returns a sorted version of the numbers with the smallest number first and the largest last. The function works by first splitting the input string into a list of numbers, converting each list element to an number using the int() function, sorting the resulting list of numbers from smallest to largest, and finally joining the sorted list of numbers back into a string.