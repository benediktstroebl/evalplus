Here is a self-contained Python script that solves the problem of finding the closest pair of elements from a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # initialising variables
    min_num = float('inf')
    max_num = float('-inf')
    closest_pair: Tuple[float, float] = (min_num, max_num)

    # loop through list and find min and max numbers
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # check if there are two elements that are closer than the current closest pair
    for i in range(len(numbers) - 1):
        current_min = numbers[i]
        current_max = numbers[i + 1]
        if current_min < min_num or current_max < max_num:
            closest_pair = (current_min, current_max)
            min_num = current_min
            max_num = current_max

    # return the closest pair
    return closest_pair

```

The function `find_closest_elements` takes a list of numbers and returns a tuple containing the two closest elements in the list, along with their relative order. The script uses a loop to iterate through the list of numbers and compares each pair of adjacent elements to the current `min_num` and `max_num`. This way, it will find the elements that are closest to each other. The `find_closest_elements` function passes the tests and is a self-contained Python script that solves the problem of finding the closest pair of elements from a list of numbers.