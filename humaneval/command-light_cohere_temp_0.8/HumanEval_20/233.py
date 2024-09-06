```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each other and return them in order (smaller number, larger number).

    : returns a tuple with the two closest numbers in that order
    """
    # initialize two variables to store the smallest and largest number in the list
    smallest = float('inf')
    largest = float('-inf')

    # loop through the list of numbers
    for num in numbers:
        # update the smallest and largest number if a smaller number is found
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # return the two closest numbers
    return smallest, largest
```
This Python code defines a function called `find_closest_elements` that takes a list of floating-point numbers as input and aims to find and return the closest pair of numbers from the list. It employs two variables, `smallest` and `largest`, initialized with the value of `inf` and `-inf` respectively, to keep track of the smallest and largest numbers encountered so far in the list. The function uses a loop through the list to compare each number with the current `smallest` and `largest` values. If a smallest number is smaller than the current `smallest`, it updates the `smallest` value. Similarly, if a largest number is larger than the current `largest`, it updates the `largest` value. After the loop completes, the function returns the `smallest` and `largest` values, representing the closest pair of numbers in the list.