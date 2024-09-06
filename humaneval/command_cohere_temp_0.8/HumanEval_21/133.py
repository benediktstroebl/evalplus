Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) * 1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. 
Here is an example:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
The script passes the test case provided in the prompt and should handle other input lists correctly. 
This solution uses list comprehension to compute the relative values of each element based on the minimum and maximum values of the input list. 

This approach provides a clear and concise solution to the problem, and it can be easily executed and understood by others with Python expertise.  If there are any further questions or more complex problems that require assistance feel free to ask!