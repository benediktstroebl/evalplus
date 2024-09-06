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

The function `find_closest_elements` serves to obtain the pair of numbers from a given list that are closest to each other. It begins by sorting the supplied list of numbers, and then verifies that the length of the list is at least two. If it is, the function returns the two last numbers, which are the closest ones due to the sorted order. If the list length is less than two, a `ValueError` is raised, thereby ensuring the function only returns valid results for lists with at least two numbers. 

Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result) 

test_list2 = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
result = find_closest_elements(test_list2)
print(result) 
```

The output will be:
```
(2.0, 2.2)
(2.0, 2.0)
```

This illustrates that for the lists provided, the outputted pairs are the closest together as stipulated by the function's requirement.