Here is a self-contained Python script that solves the problem:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Selects two numbers from a supplied list of numbers (of length at least two) that are the closest to each other and returns them in order (smaller number, larger number).
    >>> [1.0, 2.0, 3.0, 4]
   2)

	If the list is empty, it returns None, and ValueError is raised.
- If the list has one element, it returns that element and raises ValueError.
 - If the list has two elements, it selects the smaller one and raises ValueError.
"""

if len(numbers) < 2:
	return None, ValueError("List must contain at least two numbers")

elif len(numbers) == 2:
	return numbers[0], ValueError("Can't return two elements from a list of size 2")

else:
	smallest, largest = numbers[0], numbers[-1]
	for i in range(len(numbers) - 2, -1, -1):
		current = numbers[i]
		if current > largest:
			largest = current
		if current < smallest:
			smallest = current
	
	return smallest, largest

```

This function will return a tuple of the two numbers that are closest to each other, or raise an error if the input list is invalid.