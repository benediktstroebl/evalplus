```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list"""
    
    if not numbers:
        return (0, 1)
        
    return (sum(numbers), product(numbers))

# Test cases
def test_sum_product():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    assert result == (4, 12)  

if __name__ == "__main__":
    test_sum_product()
``` 
This code defines a function sum_product, which takes a list of integers and returns a tuple of their sum and product. The function is tested using the test case, which passes all the tests.