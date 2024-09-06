Here's a self-contained Python script that solves the problem of scaling Markdown code blocks using the rescale_to_unit function:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    # Sort the list in ascending order
    numbers = sorted(numbers)

    # Apply the linear transformation
    transformed_numbers = [0] * numbers[0] + numbers[1]
    
    # Create a new list with the transformed values
    return [x for x in transformed_numbers]

def test_rescale_to_unit(numbers: List[float]) -> None:
    """ Test the rescale_to_unit function

    # Provide the list of numbers
    input_numbers = [1.0, 2.0, 3.0, 4.0, 5]

   
    original numbers

    # Call the function with the list of numbers
    transformed_numbers = rescale_to_unit(input_numbers)

    # Check if the number of elements in the transformed list matches the expected number
    assert len(transformed_numbers) == 5

    # Check the transformed values
    assert transformed_numbers[0] == 0 and transformed_numbers[1] == 1 and transformed_numbers[2] == 2 and transformed_numbers[3] == 3 and transformed_numbers[4] == 4 and transformed_numbers[5] == 5

    assert transformed_numbers[0] != input_numbers[0] and transformed_numbers[1] != input_numbers[1] and transformed_numbers[2] != input_numbers[2] and transformed_numbers[3] != input_numbers[3] and transformed_numbers[4] != input_numbers[4] and transformed_numbers[5] != input_numbers[5]

if __name__ == "__main__":
    # Test the function with a list of numbers
    numbers = [1.0, 2.0, 3.0, 4.0, 5]

    original numbers

    # Call the test function with the list of numbers
    test_func(numbers)

    # Output the results
    print(numbers)
    print(test_func(numbers))
```

This script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest number is 1. The script also includes a test function `test_rescale_to_unit` that tests the `rescale_to_unit` function by passing a list of numbers and checking that the function returns the expected output.