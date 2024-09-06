```python
def sort_numbers(numbers: str) -> str:
    numbers = [int(char) for char in numbers.split()]
    numbers.sort()
    return ' '.join(map(str, numbers))
```
This Python script defines a function called `sort_numbers` which takes a string containing a sequence of numbers and sorts it in ascending order. The function splits the input string into individual numbers, converts them to integers, sorts the list of integers, and then joins the sorted numbers back into a string. This process ensures that the numbers are sorted in the correct order, ready for output. 
The script returns a string containing the input numbers sorted in ascending order, making it useful for sorting strings of numbers in Python programs. For example, if you have the input 'three five one', the output of this function would be 'one three five', indicating the numbers arranged in ascending order. 
This sort_numbers function is adaptable to various scenarios where sorting numbers in strings is necessary within Python programmes and can accommodate different number formats or separators without modifying the underlying logic.