```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # The first number is always the closest to itself
    closest1 = numbers[0]
    closest2 = numbers[0]
    
    for num in numbers[1:]:
        if num < closest1 or closest2:
            closest1 = num
        else:
            closest2 = num
        
    return closest1, closest2
```

This code uses the `find_closest_elements` function to find the two closest numbers in a list of numbers. The function takes a list of numbers as input and returns a tuple containing the two closest numbers in order, along with their respective indices. 

The logic used in this function involves iterating through the list of numbers and maintaining two variables: `closest1` and `closest2`, which represent the two closest numbers in the list. By comparing each number to both of these variables, we update the closest numbers until we find the two closest numbers. 

The function returns the two closest numbers in order, along with their respective indices.