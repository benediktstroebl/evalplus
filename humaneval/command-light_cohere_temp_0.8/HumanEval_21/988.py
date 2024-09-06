Here's a self-contained Python function that solves the given problem:

```python
def rescale_to_unit(numbers):
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This function takes a list of numbers and rescales each element such that the smallest number in the list becomes 0 and the largest becomes 1. It does this by dividing each number in the list by 100, effectively transforming the numbers into the range [0, 1] while maintaining their relative relationships. 

This function is self-contained, which means it does not require any external functions or classes to run.