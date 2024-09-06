Here's the solution to the problem:
```python
from typing import List
from math import sqrt

def find_closest_elements(numbers: List[float]):
    """
    the function takes a list of numbers and returns the two closest numbers in the list and their order
    """
    numbers.sort()  # reverse=True  # sort the list of numbers in ascending order
    min_dist, max_dist = float('inf'), float('-inf')
    for num1, num2 in zip(numbers, numbers[1:]):
        # calculate the distance between the two numbers
        x = num1 - num2
        y = sqrt((x * x) + (num1 * num2))**2)
        # update the minimum and maximum distances
        min_dist = min(min_dist, y)
        max_dist = max(max_dist, y)
    # find the two closest numbers and their order
    if min_dist < max_dist:
        closest_num1, closest_num2 = num1, num2
    else:
        closest_num1, closest_num2 = num2, num1
    return closest_num1, closest_num2

``` 
The Python script defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements along with their order. The function sorts the first and second halves of the input list, then iterates through the pairs of corresponding elements. It calculates the distance between the pair and updates the minimum and maximum distances. If the minimum distance is less than the maximum, the function finds the two closest elements and their order.

Finally, the function returns the two closest numbers in the list.

Note: This solution assumes that the input list contains at least two numbers. If the list contains only one number, it will only return that number.