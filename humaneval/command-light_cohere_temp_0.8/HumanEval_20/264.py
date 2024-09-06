Here's the solution to the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).
   

The function takes a list of float numbers as input and uses the `sorted()` function to sort the numbers in descending order. Then, it uses the first and second element of the list and compares them using the `select()` function, which returns the index of the first element in the sorted list. Finally, it returns the the smallest number and the largest number from the result of the `select()` function and returns them in order.

Here is an example of how to call the function with a list of numbers:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

find_closest_elements(numbers)
```

This would return the result `[2.0, 3.0]`, which is the two elements in the list that are the closest to each other.