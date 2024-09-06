```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    From a supplied list of numbers (of length at least 2), select and return two that are the closest to each other and return them in order (smaller number, larger number).

    :Return a tuple with the first and second closest numbers.
    """return sorted([n], [n for n in numbers if n != numbers[-1]])
n, m = map(lambda x: x, zip(*sorted([n for n in numbers if n != numbers[-1]])))]
return tuple(n, m)
```
This Python function, named find_closest_elements, takes a list of numbers as input and aims to return a tuple containing the two closest numbers in that list.

The function uses the sorted() function with a custom comparator to sort the list of numbers.

The comparator returns True if two elements are equal and False if the current element is smaller than the next element. The loop iterates over the the elements of the sorted list and compares the current element with the last element in the list. Finally, the closest elements is returned as a tuple.