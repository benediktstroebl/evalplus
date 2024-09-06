Here is a Python script that contains a self-contained function that solves the problem of finding the two closest elements in a list of numbers:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize closest and next variables
    closest, next = (float('inf'), float('-inf')) , (None, None)
    
    # Loop until two closest elements are found
    while len(numbers) < 2:
        # Find the current closest element
        current_num = numbers[0]
        
        # Find the next element
        for i in range(1, len(numbers)):
            if numbers[i] - current_num > next:
                next = numbers[i] - current_num
            current_num = numbers[i]
        
        # If the next element is closer than the current closest, update closest and next variables
        if next < closest:
            closest = next
            next = (None, None)
    
    # Return the two closest elements
    return closest, next
```

This function takes a list of numbers as input and uses a while loop to iterate over the list until it contains at least two elements. The function finds the maximum difference between each number in the list and the current closest element. It then updates the both variables, closest and next, to the maximum difference. Finally, the function returns the two closest elements.

It is a simple and efficient way to solve the problem of finding the two closest elements in a list of numbers, and it can be easily modified to solve the problem for different types of data and input lists.