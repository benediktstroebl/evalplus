```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This approach utilizes a set, `seen`, to keep track of unique elements encountered while iterating through the list `l`. Elements not in the set are added to the result list, which ensures only unique elements are included. Finally, the result list is sorted to obtain the expected output.

Here is a more detailed breakdown of the code:
1. `seen = set(l)` initializes the `seen` set with the first item in the list `l`, this ensures that any duplicates in the list will be caught during the first iteration.
2. `[x for x in l if not (x in seen or seen.add(x))]`: This list comprehension iterates through every item `x` in the list `l`. For each item, it checks two conditions:
    - `x in seen`: This checks if the item `x` is already in the set of seen elements.
    - `seen.add(x)`: If the item is not already seen, it adds it to the `seen` set.   
3. `result = []`: This initializes a new empty list to store the unique elements that will be returned.
4. `sorted(result)`: This ensures that the final returned list of unique elements is sorted in ascending order. 

By combining these elements, the function `unique` fulfills the requirement of returning a sorted list of unique elements from the input list. 

The unit tests for this function can be done by using Python's built-in `unittest` module. An example of a test that can be run for this function is: 
```python
import unittest

class TestUnique(unittest.TestCase):
    def test_unique_basic(self):
        # Arrange
        input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        
        # Act
        result = unique(input_list)
        
        # Assert
        self.assertEqual(result, [0, 2, 3, 5, 9, 123])
        self.assertCountEqual(input_list, result)  # Ensure all items are accounted for

if __name__ == '__main__':
    unittest.main()
```

Here, the `unittest` framework is employed to execute a test method, `test_unique_basic`, with assertions to validate the function's correctness. In this case, the test uses `self.assertEqual` to check if the result of the `unique` function is equal to the expected output, and `self.assertCountEqual` ensures that all items in the input list are present in the result, without duplicates. 

To run this test, you can save the code into a Python file (e.g., `test_unique.py`) and execute the script using the command `python test_unique.py` in your terminal. 

Thus, this approach provides a robust validation of the `unique` function against expected outcomes.