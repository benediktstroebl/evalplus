```python
def truncate_number(number: float) -> float:
    return number - int(number)
```

This function simply computes the difference between the input number and the largest integer less than or equal to the input number, which is the decimal part of the number. 

To test this function, you can call it with a floating point input and verify that the output is less than or equal to 1. Here is an example:
```python
test_cases = [
    (3.5,), 
    (0.999999999,), 
    (0.000000001,) 
]
for number, in test_cases:
    assert truncate_number(number) <= 1, f"Expected truncate_number({number}) to be <= 1, but found {truncate_number(number)}}"
``` 

This will assert that the output of the `truncate_number` function is less than or equal to 1 for all input values.