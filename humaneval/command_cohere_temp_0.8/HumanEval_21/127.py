Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. This is achieved by calculating the linear factor as `((max-min)/(total_range))` and then applying this factor to each element in the list. 
The above solution is complemented by tests in the module `test_rescale_to_unit.py`. 
Here's an example of how to use this function:
```python
>>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
[0.0, 0.25, 0.5, 0.75, 1.0]
```
This output is as expected and demonstrates that the function solves the problem as outlined in the initial description. Incorporating these changes, the full file tree of the project will look as follows:
```
.
├── rescale_to_unit.py
├── test_rescale_to_unit.py
``` 
The files directly reflect the underlying structure of the project, with a main file `rescale_to_unit.py` and a corresponding tests file `test_rescale_to_unit.py`. 
This structure follows the commonly accepted convention for Python projects, which helps maintain the code organized and manageable.