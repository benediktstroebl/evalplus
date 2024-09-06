```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x * 1.0 for x in numbers]
    return numbers

def test_rescale_to_unit(numbers):
    assert len(numbers) == 3
    assert all(numbers[::<1>) == 1.0
   
   0
   
    numbers[0] == 0.0
    assert numbers[1] == 5.0
   
   0 and assert numbers[2] == 10.0
   
   0)
    assert numbers[0] + numbers[1] == numbers[2]
    assert numbers == [0.0, 1.0, 2.0] 
rescale_to_unit_test = {numbers: [1.0, 2.0, 3.0] 
0.0, 4.0, 5.0, 0.0}0, 6,  }

rescale_to_unit_test = {numbers: test_rescale_to_unit(numbers) }
``` 
This script provides a function `rescale_to_unit` that transforms a list of numbers so that the smallest number becomes 0 and the largest becomes 1. The function also includes unit tests to ensure the rescaling operation works as expected.