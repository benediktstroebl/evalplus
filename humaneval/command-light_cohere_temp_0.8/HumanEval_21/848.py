Here is a self-contained Python script that solves the problem of scaling a list of numbers to a unit range of 0 to 1:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
This function takes a list of numbers as input and returns a list of the same numbers scaled to the unit range [0,1]. The function first applies the division operation [x / 100.0] to each number, where x is the element of the input list, to obtain a new number. The new number is then divided by 100.00 to obtain the number is then a single-digit number. 
The resulting list is then returned.