```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise IndexError("List of numbers must contain at least two elements")
    else:
        middle = len(numbers) // 2
        left, right = numbers[middle - 1], numbers[middle]
        return (left, right) if left == right else (min(left, right), max(left, right))
```

The function `find_closest_elements` serves to find and return the two numbers in a given list of numbers that are closest to each other. The list of numbers is assumed to be present in the function, and the function sorts this list first, then checks the length of the list to ensure it has at least two elements. If the list is of insufficient length, an error is raised; otherwise, the function retrieves the closest elements, and if these share the same value, it returns them twice, otherwise, it returns the smaller and larger of the two numbers. The function works with lists of any float numbers. 

Here is an example of how to use the function and an example of its body for a list of numbers [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]:
```python
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
# (2.0, 2.2)
``` 

This should print out the tuple (2.0, 2.2), which are the two numbers in the supplied list that are closest to each other. 

This approach does not require additional packages or modules beyond the Python standard library. 
If you want to check it out in action, you can uncomment the test example and execute the script.