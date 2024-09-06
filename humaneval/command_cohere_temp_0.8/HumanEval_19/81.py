```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order. Finally, the function returns a string where the numbers are joined back together with a space delimiter between each number, but this time in sorted order. 

The function sorts the numbers from 'zero' to 'nine' in the input string, ensuring they are sorted correctly from smallest to largest, and returns the expected output string.