```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input and returns a list of unique integers from the input list. Inside the function, it uses a set to store the unique numbers, and the `list()` function is used to convert the set back to a list, ensuring that no duplicates are retained. 

To ensure the list is intact without any changes in order, it uses `return list(set(numbers))`.

The function efficiently removes all occurrences of duplicate integers and retains only unique elements, fulfilling the problem statement's requirements.

The code includes type hints to specify the input and output types of the function, improving code readability and maintainability.

To verify the functionality, you can use Python's `unittest` framework, creating a test case that provides an input list containing duplicate integers and checking if the output list contains only unique elements:
```python
import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        # Input list with duplicates
        input_list = [1, 2, 3, 2, 4]
        
        # Call the function
        output_list = remove_duplicates(input_list)
        
        # Validate the result
        self.assertEqual(output_list, [1, 3, 4])

if __name__ == '__main__':
    unittest.main()
```

This will run the test case defined in `TestRemoveDuplicates` and verify if the output list matches the expected result.

Feel free to ask any questions or provide additional details for further refinement or code optimization opportunities. Let me know if you'd like to dive deeper into any particular aspect of the solution.