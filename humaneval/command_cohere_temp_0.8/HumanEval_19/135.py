```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string of numbers as input and returns a string with the same numbers sorted from smallest to largest. 

The function splits the input string into a list of integers, sorts that list, and then joins the sorted integers back into a string. This correctly solves the problem statement to sort the numbers from smallest to largest.