Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply linear transform to numbers
    numbers_res = [num / (max(numbers) - min(numbers)) + min(numbers) for num in numbers]
    return numbers_res
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = List([1.0, 2.0, 3.0, 4.0, 5])
   numbers = rescale_to_unit(numbers)

print(numbers)
```
The provided code defines a function called rescale_to_unit that takes a list of numbers and returns a new list of numbers after applying a linear transformation to that list. The function works by calculating the quotient of each number divided by the difference between the maximum and minimum of that number and adding the minimum value to the result. This effectively scales the0 number such minimum value to 0 and the maximum value to 1.

The script then defines a list of numbers and passes it to the rescale_to_unit function to solve the problem. The script prints out the results to the console.

This is a self-contained Python script that solves the problem of scaling a list of numbers to the unit range of 0 to 1.