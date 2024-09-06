```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers) = sorted(numbers)
    
    # Find the two closest numbers
    left, right = 0, 1
    while left < len(numbers) - 1 and right < len(numbers) - 1:
        if numbers[left] > numbers[right]:
            left += 1
        else:
            right += 1
        
    # Return the two closest numbers
    return (numbers[left], numbers[right])

# Example:
numbers = [1.0, 2.0, 3.0, 4, 5.0, 6, 7.0, 8]

print(find_closest_elements(numbers))
```
This Python script defines a function called find_closest_elements that takes a list of numbers as input and returns a tuple containing the two closest numbers in the list. The function uses a sorting technique to sort the list of numbers and then finds the two closest numbers. The function uses the simple logic to compare the numbers and return the closest pair in the sorted list. 

This code will help you solve the problem of finding the closest elements in a list of numbers.