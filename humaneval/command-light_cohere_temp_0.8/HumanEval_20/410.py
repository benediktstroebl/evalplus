Here is a self-contained Python script that includes a function with a self-contained operation that solves the problem you described:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    """ Returns a tuple of the two closest numbers in the list, ordered by their magnitude """
    smallest = float('inf')
    largest = float('-inf')
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    if smallest == largest:
        continue
    return smallest, largest
```

This Python code defines a function called `find_closest_elements` that aims to find the closest pairs of elements within a list of floats. The function takes a list of numbers as its parameter and iterates through the list to find the smallest and largest elements. If the smallest and largest elements are already found, the function continues iterating. 

The function uses the `smallest` and `largest` variables to keep track of the smallest and largest elements found so far.  The variable is set to `float('inf')` to ensure that any number is initially considered larger than any other number. 
Similarly, it sets `largest` to `float('-inf')` to ensure that any number is initially smaller than any other number. The function then iterates through the list, comparing each number with the current `smallest` and `largest` values. If a smallest and largest are equal, the function continues to the next number in the list.