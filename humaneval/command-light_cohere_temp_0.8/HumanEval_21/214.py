```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    numbers = [n / 100 for n in numbers]
    return numbers

# Test cases
test_cases = [
    [
        [0.5, 4.0],
       
        [
        [0.5, 2.0, 0.0],
       
   8, [0.1, 1.0, 5], [0.5, 5, 0.0], [0.5, 2.0]
    test other cases that are passed to rescale_to_unit function.

print(rescale_to_unit(test_cases))
```

The output of the function is the resulting list of numbers that have been rescaled to the unit [0, 1].