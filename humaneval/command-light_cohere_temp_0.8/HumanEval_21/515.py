Here is a self-contained Python script with a function that solves the problem you have described:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Initialize the modified list
    modified_numbers = numbers[:]

    # Loop through the original list
    for num in numbers:
        # Apply the rescaling factor to the current number
        modified_numbers.append(num * (1.0 / num))

    modified_numbers.append(num)

    # Return the modified list
    return modified_numbers
```

The provided code defines a rescale_to_unit function that takes a list of numbers as input. The function then creates a new list called modified_numbers, which initially contains the same values as the input numbers list. 

The function then loops through the input list and applies the rescaling factor to the current number. The current number is multiplied by the reciprocal of its previous value in the list. 

Finally, the function appends the current number to the modified list and returns the updated list.