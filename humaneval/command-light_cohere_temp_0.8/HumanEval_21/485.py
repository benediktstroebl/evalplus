Here's a self-contained Python script with a function that solves the problem:

```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers in the list, such that the smallest number becomes 0 and the largest becomes 1
    numbers[0] = 0
    numbers[1] = 1
    for i in range(2, len(numbers)):
        numbers[i] = (numbers[i-2] / numbers[i-2]) * numbers[i]
    return numbers
```

This function, `rescale_to_unit`, takes a list of numbers as input and returns a new list with the same numbers but with values rescaled to the range [0, 1]. The function works by first making the first number in the list 0 and the second number 1. Then, for each remaining numbers in the list, it computes a value based on the formula (number / smallest_number) * largest_number, which effectively scales the number up by multiplying it by the product of the largest and smallest number, and then divides it by the smallest number. 
Finally, the function returns the new list of numbers with the desired rescaled values.