Here's the provided self-contained Python function:
```python
def rescale_to_unit(numbers: List[float]):
    return [x / min(numbers) for x in numbers] if len(numbers) > 1 else numbers]
```
This function first takes a list of numbers and then divides each element by the minimum number in the list. This effectively scales all numbers down to the range 0 to 1, which is the typical unit for a list of floating-point numbers. 
Note that the minimum value is determined using the min() function, and the list is then returned if it has more than one element.