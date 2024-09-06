```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    - If numbers: list of float, the list of numbers to be rescaled.
    - Return a numbers in the same scale, such that the smallest element is 0 and the largest is 1.
    """
    test_case = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    assert numbers[0] == 0
    assert numbers[0] == 1
    assert numbers[1] == 0
    assert numbers[1] == 1
    assert numbers[2] == 0
    assert numbers[3] == 1
    assert numbers[4] == 0
    assert numbers[5] == 1
    assert numbers[6] == 0
    assert numbers[7] == 1
    assert numbers == [0.0, 1.0, 0.0, 0.0, 1.0]

   0, 7]  # Test case success
    ```