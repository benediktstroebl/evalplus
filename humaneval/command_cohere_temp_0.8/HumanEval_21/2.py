Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers `numbers` as input and returns a transformed list. The transformation is a linear normalization that maps the smallest number in the input list to 0 and the largest number to 1. This is achieved by calculating the difference between each number `x` and the minimum of the list, divided by the difference between the maximum and the minimum, yielding `[0.0, 0.25, 0.5, 0.75, 1.0]` for the test input `[1.0, 2.0, 3.0, 4.0, 5.0]`.

Here's a test case that can be used to verify the function:
```python
def test_rescale_to_unit():
    # Initial list with at least 2 elements
    input_lst = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected_rescale = [0.0, 0.25, 0.5, 0.75, 1.0]

    # Function call and comparison
    rescaled = rescale_to_unit(input_lst)
    assert rescaled == expected_rescale
```
This test case verifies if the output of the function matches the expected normalized list. 
To run the test, you can use the `pytest` framework, which can be installed via `pip install pytest`, and then call `pytest` in the terminal. 

The `'rescale_to_unit'` function can be imported and used in other Python scripts, and is designed to work independently, making it portable and easy to integrate into various projects.  If you encounter any issues or have further questions, feel free to ask!