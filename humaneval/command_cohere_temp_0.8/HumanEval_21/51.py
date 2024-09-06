Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    rescaled_numbers = [0 if number == min(numbers) else (number - min(numbers)) / (max(numbers) - min(numbers)) for number in numbers]
    return rescaled_numbers
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers rescaled to the range [0, 1] based on the smallest and largest values in the input list. This function can be used to normalize data for analysis or visualization. Test files are not included as part of the code snippet, but given the simplicity of the function, it does not require elaborate testing to ensure its correctness.