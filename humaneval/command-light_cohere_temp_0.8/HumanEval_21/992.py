Here is a self-contained Python script that solves the problem of scaling numbers within a given list to unit values of 0 to 1:
```python
def rescale_to_unit(numbers: List[float]):
    return [x * 1.0 for x in numbers] if __name__ == "__main__"; else numbers
```

This function takes a list of numbers and returns a new list where each value has been rescaled to the unit values of 0 to 1. It uses the same if the name of the function is "main", which is the typical way of using a function within a script. This way allows to test the function from the script without needing to import it.