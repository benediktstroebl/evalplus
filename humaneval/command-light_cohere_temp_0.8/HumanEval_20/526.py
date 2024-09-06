```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    """ 
    Returns the two closest numbers from a list, in order of smaller number, larger number.

tests:
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2]) == (2.0, 1.0)
    result:
          assert find_closest_elements([1.0, 2.0, 3.2]) == (1.0, 2)
    result:
          assert find_closest_elements([1.0, 2.0, 3.2]) == (1.0, 2)
          """ result:
          assert find_closest_elements([1.0, 2.0, 3.2]) == (1.0, 2)
result:
          assert find_closest_elements([1.0, 2.0, 4.2]) == (1.0, 2)
          ``` result:
          assert find_closest_elements([1.0, 2.0, 4.2]) == (1.0, 2)
          ```

```