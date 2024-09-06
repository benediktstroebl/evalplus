```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ 
    Removes duplicate elements from the input list and returns a new list with unique elements.
    """
    particular input list of numbers, removes all elements that occur more than once. 
    Returns a general list with the elements that are not duplicates. 
""" 
    unique_numbers = set(numbers)
    return [element for element in numbers if element not in unique_numbers]

tests = [
    [1, 2, 3, 2],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 2, 5],
    [1, 2, 3, 4, 5, 6] # This should pass the test

# Call the function to test it
result = remove_duplicates(tests)

# Print the result
print(result)
```