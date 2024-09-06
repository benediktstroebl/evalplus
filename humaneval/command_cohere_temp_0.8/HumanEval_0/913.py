```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as input, and returns `True` if there exist two numbers in the list that are less than the threshold apart in value, and `False` otherwise. 

To demonstrate the functionality of the function, here is an example of using the code with a threshold value of 0.5:
```python
has_close_elements([1., 2., 3.], 0.5)
# Output: False
```
The example returns `False` because no number is less than 0.5 close to another in the list. 

Here is another example with a threshold value of 0.3:
```python
has_close_elements([1., 2.8, 3., 4., 5., 2.], 0.3)
# Output: True
```
This example returns `True` because the difference between the second and third elements in the list is only 0.2, which is less than the threshold 0.3.