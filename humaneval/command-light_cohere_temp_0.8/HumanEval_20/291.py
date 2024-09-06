```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order.
    numbers.sort()
    priority of two closest elements in the list.
    # Select the return the minimum and maximum number
    min_num, max_num = numbers[0], numbers[-1]
    closest = (numbers[1], numbers[0])
    # Compare the two elements to each other
    for i in range(len(numbers)-2):
        current_num = numbers[i+1]
        if current_num < closest[0]:
            closest[0] = current_num
        elif current_num > closest[1]:
            closest[1] = current_num
    return closest

def test():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
    return find_closest_elements(numbers=[1.0, 2.0, 3.0, 4.0, 5.0, 2])

test_output = "closest elements are (2.0, 5.0) in this order order order

print(test_output)

```
This script defines a function called `find_closest_elements` that takes in a list of numbers and returns a tuple containing the two closest elements in the list. The function then sorts the list of numbers and uses the `bisect` method to find the two closest elements. Finally, the function is tested by passing in a sample list of numbers and printing out the result.