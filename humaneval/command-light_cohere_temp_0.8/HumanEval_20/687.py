```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize two lists to hold the closest elements
    closest1 = [float('inf')]
    closest2 = [float('-inf')]

    # Initialize two variables to hold the closest elements
    first_index = 0
    second_index = 0

    # Loop through the list of numbers
    for index, num in enumerate(numbers):
        if num < numbers[first_index]:
            closest1[first_index] = num
        elif num > numbers[second_index]:
            closest2[second_index] = num
        else:
            # Swap the closest elements
            closer = min(closest1, closest2)
            closer_index = index
            if closer_index == first_index:
                first_index = second_index
            else:
                second_index = first_index

        # Move the second variable to the correct index
        if closer_index == first_index:
            second_index = closer_index + 1

    # Return the two closest elements and their order
    return closest1[first_index], closest2[second_index]

# Test
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
return find_closest_elements(numbers), "Success")
```

The code defines a function called `find_closest_elements` that takes a list of numbers as an argument and returns a tuple containing the two closest elements in the list, along with their order. The function uses a two lists, `closest1` and `closest2`, to keep track of the two closest elements as it iterates through the input list. The function also uses two variables, `first_index` and `second_index`, to keep track of which element is the closest to which at the current index. 

Finally, the function swaps the two elements in `closest1` and `closest2` and moves the second variable to the correct index, so that the variables correctly keep track of the closest elements.