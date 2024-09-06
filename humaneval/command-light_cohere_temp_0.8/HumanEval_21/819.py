```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the rescaling function
    numbers_rescaled = [x / min(numbers) for x in numbers]
    return numbers_resc

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_unit(numbers)
```

The script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list with the same numbers but rescaled to the unit range [0,1]. The `min` function is used to find the smallest number in the input list, and then each number in the list is divided by this smallest number to obtain the rescaled value. The `numbers_rescaled` variable is used to store the result of the division operation. 

The function can be used to solve the problem by passing a list of numbers as an argument to the `rescale_to_unit` function, and the result is stored in the `numbers_rescaled` variable.