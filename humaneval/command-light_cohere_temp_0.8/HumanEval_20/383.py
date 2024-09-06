```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)

    # Find the two closest elements
    smallest, largest = (numbers[0] , numbers[-1])
    for i in range(1,len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
        elif numbers[i] > largest:
            largest = numbers[i]

    # Return the two closest numbers
    return smallest , largest
```
The provided code defines a function called `find_closest_elements` that takes a list of numbers as input and returns a tuple containing the two closest elements from the list. 

This is accomplished by first sorting the input list of numbers and then iterating through the sorted list to find the two closest elements. 

Finally, the code returns the two closest elements in order, with the smaller element first. 

This is a self-contained Python function that solves the problem of finding the two closest elements in a list of numbers.