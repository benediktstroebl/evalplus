Here is the Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("At least two elements required")
    a, b = (numbers[0] if len(numbers) == 2 else min(numbers), max(numbers))
    return a, b

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
a, b = find_closest_elements(numbers)
	print("The closest elements are:", a, b)

```
The find_closest_elements function takes a list of numbers as input and returns a tuple with the two closest elements in it. The function first checks if the list has at least two elements. If not, a ValueError is raised. The function then uses the min and max functions to find the two closest elements, a and b. The function then returns the two elements in order. The output of the code is the following:
```python
print("The closest elements are:", find_closest_elements([1.0, 2.0, 3.0, 4]))
```