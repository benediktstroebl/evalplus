```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
This Python script defines a function `rescale_to_unit` which takes a list of numbers as input and returns a list of numbers rescaled to the range [0, 1]. The `typing` module is used to declare the input parameter as a list of floats, and the `List` annotation specifies that the function returns a list of floats. Within the function, the minimum and maximum values of the input list are calculated using the `min` and `max` functions, respectively. Then, a list comprehension is used to apply the linear transformation to each element of the input list.

To ensure the functionality of the code, it is recommended to include tests. Here is an example of test cases using the `unittest` module:
```python
import unittest

from rescale_to_unit import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])

    def test_rescale_to_unit_with_single_element(self):
        self.assertEqual(rescale_to_unit([10.0]), [1.0])

    def test_rescale_to_unit_with_multiple_elements(self):
        self.assertEqual(rescale_to_unit([2.0, 5.0, 8.0]), [0.0, 0.5, 0.67])

if __name__ == '__main__':
    unittest.main()
```
In the above code, the `unittest` module is imported, and a test class `TestRescaleToUnit` is defined, which inherits from `unittest.TestCase`. Three test methods are defined: `test_rescale_to_unit`, `test_rescale_to_unit_with_single_element`, and `test_rescale_to_unit_with_multiple_elements`. Each test method verifies the output of the `rescale_to_unit` function against the expected output using the `self.assertEqual()` method. Finally, `unittest.main()` is called to discover and run the test cases. 
The code will only execute the test cases if you run the script containing this code separately, or incorporate it into your testing/validation pipeline. 

Feel free to customize the test cases to cover more scenarios or use other testing techniques and frameworks to suit your needs. GPORTFHOUOHJFKJGFBJMJVWVQERUVLJQHLMQJGCFC PIUEYHMJRFFAKJHHAFYAWYYJXHKDWZJKHOCZDUGCGCNQPLLIJWNYZKXLGHKJHHAFYAXHXHQWHJHZJWQE HJZKAFHJJWQEYHJTGMFRXVRUHZFHJKHDTYMKHKBHMRGHZFUCDPGTLLNQPFMHJUHZGURPKLMKHRSEHRHZN WXUQWKHSRHRURMHJEHZRHQMKRGDUEYDZRHRMMZBHMKHR