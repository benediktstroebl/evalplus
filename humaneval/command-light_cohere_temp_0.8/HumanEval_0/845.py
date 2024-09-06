```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.8)
   equal(0.5, 0.5, return True)
   
    <br> 
    >  has_close_elements([1.0, 2.0, 3.0], 0.8)
    time < close
     > has_close_elements([1.0, 2.8, 3.0], 0.8) 
    <9return at[1.0, 2.8, 0.0], 0.1)
   8 return
   0.0)
   time.0 <= 1.0 <= 2.8) 
    < hastime.5
   return True
```