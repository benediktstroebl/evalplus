```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
   gees([1.0, 2.0], 0.2) with threshold 0.4
   
   0.0)
   0.2)
   
return True)

>>> test_data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
has_close_elements(test_data, 0.0)  # True

```
The function has_close_elements takes a List[float] called numbers and a float threshold as input. It returns a bool value. The function checks if in the numbers list, are any two consecutive elements closer to each other than the threshold. It then returns True.  If time, the function passes the corresponding tests and gets the following output:
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0] -> has_close_elements([1.0, 2.0], 0.2)