```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize two lists to hold the closest and farthest elements
    closest_elements = [float('inf')] , float('-inf')]
    for num in numbers:
        # Compare the current number to the current closest and farthest elements
        if num < closest_elements[0]:
            closest_elements[1] = num
            closest_elements[0] = num
        elif num > closest_elements[1]:
            closest_elements[0] = num
            closest_elements[1] = num
    else:
        # If no clear winner, reset the lists
        closest_elements[0] = float('inf')
        closest_elements[1] = float('-inf')
    return closest_elements

def test_find_closest_elements(numbers_list: List[float]):
    result = find_closest_elements(numbers_list)
    assert(result[0] == result[1])
    assert(result[0] < numbers_list[0])
    assert(result[1] > numbers_list[0])
    assert(result[0] < numbers_list[1])
    assert(result[1] > numbers_list[1])

# Example usage
numbers_list = [1.0, 2.0, 3.0, 4.0, 5.0]
print_find_closest_elements(numbers_list)
```
This code defines a function `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers in the list. The function initializes two lists, `closest_elements[0]` and `closest_elements[1]`, to hold the smallest and largest numbers, respectively. After looping through numbers, the function compares each number with the current smallest and largest numbers and updates the lists accordingly. The function then checks that the current number is the closest to the current smallest or largest number, and if not, it updates the list accordingly. Finally, the function returns the list of the two closest numbers. The code also defines a function `test_find_closest_elements` that takes a list of numbers as input and calls the `find_closest_elements` function with this list as an argument. It then asserts that the results are correct, meaning that the function returns the correct two closest numbers in the list.