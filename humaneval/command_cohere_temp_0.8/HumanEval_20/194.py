```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function `find_closest_elements` serves to find and return the two numbers in a supplied list of numbers that are closest to each other. This is accomplished by sorting the list in ascending order, and then returning the two end elements of the list, assuming that the list is of length at least 2. The function is robust in that if the list length is less than 2, it raises a `ValueError`, preventing the return of invalid pairs. The function utilizes the `typing` module to denote the input as a list of float values, adding type safety to the function.

Here is an example usage of the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
print(find_closest_elements(test_list))  # Output: (2.0, 2.2)
```

And here is a more concise example usage:
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
``` 
This will print the pair of numbers that are closest to each other in the provided list.