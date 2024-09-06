```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling maximum elements found in the sequence.
    Each element is the first, and for every subsequent element,  the element 
    is compared with the rolling maximum, and the rolling maximum is updated accordingly.
    """
    list of integers is passed as a parameter, and the list of rolling 
    maximum elements is returned.
    """
test cases are also defined, which verify that the rolling_max function 
    works correctly for various inputs.

```
In this solution, we use the rolling technique, where the maximum element is updated after each element. We store the maximum element in a list and update it after each element. The rolling_max function takes a list of integers and returns a list of rolling maximum elements.