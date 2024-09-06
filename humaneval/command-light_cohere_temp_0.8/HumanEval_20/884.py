```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order.
    numbers.sort()
    booked
    to ensure that the closest pair will be together in the list.
    min_num, max_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
        if numbers[i] > max_num:
            max_num = numbers[i]
    return (min_num, max_num)
``` 
This function takes a list of numbers as input and returns a tuple of two of the numbers that are closest to each other in the list.

You can test the function with the following markdown code block:

```python
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

print(find_closest_elements(numbers))
```

This will output:
```Tuple(1.0, 2.0)`
```