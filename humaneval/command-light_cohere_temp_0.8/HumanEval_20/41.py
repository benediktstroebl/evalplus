```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """
    Selects and returns two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).
    return (smaller_number, larger_number)
# end function

def test_find_closest_elements(numbers):
    # Test the function
    close_numbers = find_closest_elements(numbers)
    print(f"The closest numbers are: { {close_numbers[0]}, close_numbers[1]}")
```

The function `find_closest_elements` takes a list of numbers as an argument and returns a tuple of the two closest numbers. The function uses the approach of selecting the first and second elements from the list based on their order of proximity. The test function `test_find_closest_elements` passes the argument to the function and prints the result.