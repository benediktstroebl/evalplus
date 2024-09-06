Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. The `typing` module is used to define the input type as `List[float]`.

To test this function, you can execute the following code:
```python
import unittest
test = unittest.TestCase()

test.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
test.assertEqual(rescale_to_unit([5.0, 4.0, 3.0, 2.0, 1.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
```
The first test asserts that the function scales the values correctly when the largest value is 1.0 and the smallest value is 0. The second test asserts that the function correctly scales values when the largest value is 5.0 and the smallest value is 1.0. Feel free to add more test cases to cover different scenarios and ensure the function's correctness. 
The code should yield the following markdown:
```python
```
You can include this code within a code block in Markdown to demonstrate the problem solution. In this case, the Markdown renderer should display the code with light markup.