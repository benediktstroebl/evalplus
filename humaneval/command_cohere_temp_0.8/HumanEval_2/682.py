```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply subtracts the largest integer that is less than the input `number`, which effectively captures the leftover decimal part. 

You can test this function using the example provided in the original prompt:
```python
truncate_number(3.5) == 0.5
```

The code above confirms that the function behaves as expected, returning `0.5` when applied to the input `3.5`.  This approach is straightforward and works for achieving the desired result.