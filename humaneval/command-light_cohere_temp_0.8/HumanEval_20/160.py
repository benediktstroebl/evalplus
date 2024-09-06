```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Get the two numbers with the smallest and largest values respectively and return them in order
    return (numbers[0], numbers[-1])
```
This function takes a list of numbers as input and returns a tuple of two adjacent numbers in the list that are the closest to each other. The function first sorts the words in ascending order, and then uses the sorted list to find the two numbers with the smallest and largest values respectively.