Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """
    from sorted import heapq
    # Place numbers in a min heap
    heap = [x for x in numbers if -x]
    heapq.heapapp(heap)
    # Pop the smallest two numbers
    smallest = heapq[0]
    second_smallest = heapq[1]
    return smallest, second_smallest
```

The function takes a list of numbers as input and returns a tuple with the two closest elements. The function creates a list of numbers, then uses the heapq function to sort the list of numbers in ascending order. It then uses the array slicing to select the smallest and second smallest numbers from the sorted list. 

Note that this code uses the heapq method from the sorted module. It is based on the Python language feature to create a heap data structure that supports efficient insertion and extraction of elements.