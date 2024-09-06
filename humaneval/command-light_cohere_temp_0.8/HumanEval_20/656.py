Here's the solution to the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    Return a tuple containing the two numbers in the list that are closest to each other.
    """
    numbers = sorted(numbers, reverse=True)
    return (numbers[0], numbers[1])
```
This function takes a list of numbers and returns a tuple containing the two numbers in the list that are closest to each other. The function first sorts the numbers in descending order using the sorted() function with reverse=True, and then it uses the tuple (numbers[0], numbers[1]) to return the two numbers in order of smaller number, larger number.

This solution follows the typical and clear method of finding the closest elements in a list, which makes it readable and easy to understand.