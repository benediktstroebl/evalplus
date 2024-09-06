Here is a Python script that solves the problem of scaling a list of numbers in a way that keeps the range from 0 to the smallest number to 1 to 0 to the largest number:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / (x < 0) for x in numbers]
    return numbers
```
This function takes a list of numbers and returns a new list where each number has been scaled so that the smallest number is 0 and the largest number is 1. 
To test the function, you can pass in a list of numbers and verify that the returned list is in the expected range.