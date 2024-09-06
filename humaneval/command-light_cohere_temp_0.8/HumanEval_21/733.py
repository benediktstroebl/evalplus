Here is a self-contained Python script that solves the problem:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers.extend(1.0 / numbers[max(numbers) - 1.0)
   
numbers. = list(map(lambda x: x*100.0 if x< 0 else x/100.0 if x< numbers[-1] else 1.0))
return numbers
```

This function takes a list of numbers and rescales each value in the list such that 0 becomes the smallest number and 1 becomes the largest number. It works by applying a inverse linear transform to each number, where the transform is a simple scaling by a factor of 100. The function then returns the list of rescaled numbers.

You can test the function using the built-in `unittest` module in Python.