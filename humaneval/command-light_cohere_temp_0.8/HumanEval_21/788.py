Here is the self-contained Python script:

```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100.0 for x in numbers] + [100.0] * numbers
   0
    rescale the numbers and returns the result
```
Do you need anything else?