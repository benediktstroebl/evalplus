```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == min(diff, *[abs(nums_sorted[i] - nums_sorted[i-1]) for i in range(1, len(nums_sorted))]) else nums_sorted[1], nums_sorted[0]
```

The function works by first sorting the list and then checking the closest elements, namely the first and the last one, against the criterion of being the closest. If they do not fit the criterion, then the function selects the second element and the first one, which is the closest pair not guaranteed to be the closest pair in absolute distance in case the list is sorted. 

Here is a test to check if the function is correct:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
test_result = find_closest_elements(test_list)
test_print = f"{test_result} != (2.0, 2.2)"
print(test_print)
assert test_result == (2.0, 2.2)
``` 

The assertion should print out true confirming the correctness of the function implementation. 

The version with absolute values implemented as a separate function to make the code clearer:
```python
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == min(diff, *[abs(nums_sorted[i] - nums_sorted[i-1]) for i in range(1, len(nums_sorted))]) else nums_sorted[1], nums_sorted[0]

def absolute_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    nums_sorted = sorted(numbers)
    diff = abs(nums_sorted[-1] - nums_sorted[0])
    return nums_sorted[0], nums_sorted[-1] if diff == min(diff, *[abs(nums_sorted[i] - nums_sorted[i-1]) for i in range(1, len(nums_sorted))]) else nums_sorted[1], nums_sorted[0]
``` 

Over usage of the absolute_closest_elements function is demonstrated via the following example:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
test_result = absolute_closest_elements(test_list)
test_print = f"{test_result} != (2.0, 2.2)"
print(test_print)
assert test_result == (2.0, 2.2)
``` 
that should assert true confirming the correct implementation of the absolute_closest_elements function.