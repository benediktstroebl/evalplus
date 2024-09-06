```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order. Finally, it converts the sorted list of integers back to a string by joining the list elements with spaces and returns the result. 

This code block seems to pass the test case provided in the prompt, as well as a test case assuming the function call `sort_numbers('9 5 3 1')`, returning '1 3 5 9', which would presumably be the correct answer.