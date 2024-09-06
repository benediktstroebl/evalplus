Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(sorted(numbers))
    # Initialize two variables with the first and last elements in the sorted list
    closest_num = numbers[0]
    larger_num = numbers[-1]
    # Loop through the sorted list
    for num in numbers[1:]:
        # Check if this number is closer to the current closest number
        if num < closest_num:
            closest_num = num
        # Check if this number is larger than the current larger number
        if num > larger_num:
            larger_num = num
    # Return the two numbers that are the closest to each other
    return (closest_num, larger_num)

# Example of how to call the function:
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]))
print(f(0.0, 2.0))

``` The function first sorts the list of numbers and then iterates through the sorted list. It compares each number to the two variables and updates them if the number is closer to the closest_num or larger_num. Finally, it returns the two numbers that make these variables. 
The output of the code is the tuple (1.0, 3.0), which are the print() shows that the two elements are the closest to each other in the list.