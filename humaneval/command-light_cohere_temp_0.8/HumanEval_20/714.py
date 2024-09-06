Here is the Python script that solves the problem of finding the two elements in a list that are closest to each other:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort the list of numbers in ascending order
    numbers.sort(numbers)
    # find the two elements that are the closest to each other
    elements = [numbers[0], numbers[1]]
    for i in range(2, len(numbers)):
        if (elements[0] > numbers[i]) or (elements[1] > numbers[i]):
            elements.append(numbers[i])
    # return the elements in order of the smaller number first
    return elements

# example of usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = find_closest_elements(numbers)

This function first sorts the input list of numbers in ascending order. Then, it iterates through the list, starting from the second element, and checks if the current element is closer to either of the two elements already selected. If it is, it adds that element to the list of elements to select. Finally, it returns the list of elements in order of the smaller number first.