Here is the self-contained Python script:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)

    # Get the two elements with the smallest and largest numbers
    min_num, max_num = numbers[0], numbers[-1]
    for i in range(len(numbers) - 1):
        if numbers[i] < min_num:
            min_num, max_num = numbers[i], numbers[-i - 1]

    return (min_num, max_num)
```
This function takes a list of numbers as input and sorts the list in ascending order. Then, the two elements with the smallest and largest numbers are stored in `min_num` and `max_num` variables. The loop then checks if the number in the list is smaller than the current `min_num` value. If the current `min_num` is smaller than the current number, then the variables are updated to the current number and the previous `min_num` value.

Finally, the function returns a tuple containing the two closest elements in the list.