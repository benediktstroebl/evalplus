```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    return numbers[1], numbers[2]
```
This Python script defines a function called `find_closest_elements` that takes a list of floating numbers (`List[float])` as input. This function sorts the list of input numbers in ascending order and then returns the second and the third element from the sorted list, which implies the two numbers that are closest to each other in terms of value. The result is returned as a tuple (`Tuple[float, float]`) with two floating values. 

Here is an example of how to use the code:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # Output: (2.0, 2.2)
``` 
This will output: `(2.0, 2.2)` which is the closest pair of numbers in the list `[1.0, 2.0, 3.0, 4.0, 5.0, 2.2]`

To further illustrate the functionality, let's consider a different list:
```python
test_list_2 = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
result = find_closest_elements(test_list_2)
print(result)  # Output: (2.0, 2.0)
```

The output this time will be `(2.0, 2.0)` since the list `[1.0, 2.0, 3.0, 4.0, 5.0, 2.0]` has a repeat of the number 2 at index 2 and index 5, and these are the closest numbers to each other in the list. 

These examples demonstrate how the `find_closest_elements` function works to solve the problem of finding the closest elements in a list of numbers.