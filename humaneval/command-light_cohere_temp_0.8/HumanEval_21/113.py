Here is a Python script that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Initialize the output list
    output_list = [0.0]
    
    # Loop through all numbers
    for num in numbers:
        output_list.append(num / 100.0)
    
    # Return return the _ list(output_list)
    ```

You can test the function with a list of numbers, like this:
```python
# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0])
```