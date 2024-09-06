```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.resize(lambda x: (x - min(x)) / (max(x) - min(x)))
    return numbers

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print("Output is : [0.0, 0.0, 0.0, 1.0]")

numbers = [0.1, 0.0, 0.0, 0.0, 0.0]
print("Output is : [0.0, 0.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 0.0, 0.0]")
print("Output is : [0.0, 1.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 1.0]")
print("Output is : [0.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 0.0]")
print("Output is : [0.0, 0.0, 1.0]")
 print("Output is : [0.0, 0.0, 1.0]")
 print("Output is : [0.0, 1.0, 1.0]")
 print("Output is : [0.0, 0.0, 0]")
```