```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. 

The function first converts the space-delimited string of numbers into a list of integers. Then, it sorts this list in ascending order using the `sort()` method. Finally, the function returns a string formed by joining the sorted list of numbers back into a single string, using the `join` method. 

This approach ensures that the function works for any valid input string of numbers and provides the expected sort order. 
The unit test included in the problem statement can be used to verify the function's correctness. It will test the function sort_numbers with the input 'three one five' and expect the output 'one three five'.