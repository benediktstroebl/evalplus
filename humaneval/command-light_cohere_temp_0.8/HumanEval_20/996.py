Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the input list in ascending order
    sorted_numbers = sorted(numbers)

    # Find the first two elements in the sorted list
    first_two = next(sorted_numbers)

    # Initialize variables to keep track of the smaller and larger numbers
    smaller = first_two[0]
    larger = first_two[1]

    # Iterate through the remaining elements in the sorted list
    for num in sorted_numbers[2:]:
        # Calculate the distance between the current number and the previously calculated smaller and larger numbers
        distance = abs(num - smaller) + abs(num - larger)

        # If the distance is smaller than the previously recorded distance, update the smaller and larger numbers
        if distance < (distance of smaller + distance of larger):
            smaller = num
            larger = num

        # If the smaller number is larger than the larger number, update the result variables
        if num > larger:
            result = (smaller, larger)
            break

    # Return the final result
    return result
```
This function takes a list of numbers as input and returns a tuple containing the two closest elements. It uses the simple list sorting and then iterates through the list to find the closest pairs of elements.