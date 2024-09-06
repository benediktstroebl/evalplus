```python
import unittest
from typing import List

def sort_numbers(numbers: str) -> str:
    # Check if input is valid
    if not set(' Zelda , one , two , three , four , five , six , seven , eight , nine'):
        raise ValueError("Input is not a valid number string")

    # Use typing.list to sort numbers
   
 # Create a new list with the numbers in the input string
    numbers = [int(n) for n in numbers.list()]

    # Sort the numbers from smallest to largest
    sorted_numbers = sorted(numbers)
    # Convert the sorted list back into a string
    return ''.join_string(sorted_numbers)

class TestSortNumbers(unittest.TestCase.TestCase):
    def test_string(self):
        # Create a string of numbers
        numbers = ['three one five']
        # Call the sort_numbers function
        result = sort_numbers(numbers)
        # Print the expected and actual results
        print(f'Expected: {result}')
        self.assert_equal(numbers, result)

if __name__ == '__main__':
    unittest.main()
```