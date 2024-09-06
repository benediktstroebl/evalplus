```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # Extract the first and second elements of the sorted list
    first_element, second_element = sorted_numbers[0:1]
    
    # Compare the first elements and return the smaller one
    if first_element < second_element:
        return (first_element, second_element)
    else:
        return (second_element, first_element)

# Test the function with an example list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
0, 1.5)
print(find_closest_elements(numbers))
``` 
The provided code defines a function `find_closest_elements` that takes a list of numbers as input and aims to find the pair of the two closest elements in the list, such that the smaller element comes first. 

The function first sorts the list of numbers in ascending order using the `sorted` function and assigns the first element of the sorted list to a new variable `first_element` and the second element to `second_element`.

The function then compares the `first_element` and `second_element` using an `if` statement. If the `first_element` is less than the `second_element`, it returns a tuple with the values of `first_element` and `second_element`, indicating the closest elements. 

If the `first_element` is greater than or equal to the `second_element`, it returns a tuple with the value of `second_element` and `first_element`, indicating that they are the closest elements in the list. 
This code follows the principles of finding the closest elements and provides a clear and readable structure for solving the problem.