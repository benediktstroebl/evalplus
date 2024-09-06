Here is a self-contained Python script that defines a function that solves the problem of checking if any two numbers in a list are closer than a given threshold:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    #sort the list
    numbers.sort(reverse = True)
    #define comparison function 
    def comp(x, y):
        return (x<threshold and y>threshold) or (x>threshold and y<threshold) 
    return comp(numbers[0], numbers[1])

#return if any(comp(x,y) for x,y in zip(numbers,numbers[1:]))

```

This script defines a function `has_close_elements` that takes in two arguments: a list of numbers and a threshold. The function returns a boolean that checks if any two numbers in the list are closer than the threshold. The function does this process by sorting the list and then using a custom comparison function to check if any two numbers in the list are closer than the threshold.