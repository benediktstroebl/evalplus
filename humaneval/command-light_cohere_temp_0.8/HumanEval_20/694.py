Here's a Python script that follows your request:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initial sorting
    numbers.sort(numbers, key=lambda x: x)
    # two closest elements
    smallest, second_smallest = (numbers[0], numbers[1])
    # loop to find next smallest pair
    while smallest != second_smallest:
        smallest = numbers[0]
        second_smallest = numbers[1]
        # move one element
        i = 0
        while i < len(numbers) - 1:
            if numbers[i] < smallest:
                smallest = numbers[i]
                second_smallest = numbers[i+1]
                i += 1
            elif numbers[i] > second_smallest:
                second_smallest = numbers[i]
                i += 1
        else:
            break
    return smallest, second_smallest
```
The function "find_closest_elements" takes a list of numbers as input and returns a tuple with the two closest numbers to each other, or throws an error if the list is empty.

This function uses the built-in sorting function from the Python list module to sort the list of numbers. The function then uses a two-pointer technique to keep track of the two closest elements and their order. 
Finally, the function returns the two closest elements in the order of the smaller number.