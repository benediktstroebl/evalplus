Here is a self-contained Python script that solves the problem you have provided:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple containing the two closest elements from the list and their relative order.
    
    - Find the smallest element in numbers
    - If there is only one, return that element as the first part of the tuple
    - If there are two, compare the elements and return the larger one as the first element of the tuple
    - Return the tuple as the result
    """
    smallest = float('inf')
    largest = float('-inf')
    for num in numbers:
        if smallest > num:
            smallest = num
        if largest < num:
            largest = num
    return smallest, largest
```

This function takes a list of numbers as input and returns a tuple containing the two closest elements from the list and their relative order. The function uses a same time algorithm to find the closest elements, which is a simple comparison of the current element with the smallest and largest elements found so far. 

Please note that this function assumes the input list has at least two elements.