Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers)) * 1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers and transforms them using simple mathematical operations to create a new list where the smallest number is 0 and the largest number is 1. This is done by calculating the ratios of each element to the range (max-min) of the input list. The result is a linear transformation of the input list. 
The script does not include automated tests as there are no simple assert statements to verify the solution, however, the function is easily testable with the example provided in the problem statement.
The solution is efficient and will not perform poorly on large inputs since it is a simple linear calculation for each element in the list. Do you need assistance with any other programming problems? It would be great to dive deeper into any specific topic you'd like to understand better.