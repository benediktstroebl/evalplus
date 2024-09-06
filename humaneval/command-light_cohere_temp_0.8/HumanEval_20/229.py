Here is a self-contained Python script with a function that solves the problem:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Find the two closest numbers
    first_index = bisect_left(sorted_numbers)
    second_index = bisect_right(sorted_numbers)
    closest_pair = (sorted_numbers[first_index], sorted_numbers[second_index])
    
    return closest_pair

def main():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
   
    return find_closest_elements(numbers=list(map(int, input() for _ in input())))
```

This code is a complete Python program that includes a function `find_closest_elements` that accepts a list of numbers as input and returns a tuple containing the two numbers that are the closest to each other. The main function is then defines a list of numbers, passes it to the `find_closest_elements` function, and prints out the result.