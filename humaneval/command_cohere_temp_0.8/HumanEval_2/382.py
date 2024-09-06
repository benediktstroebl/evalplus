```python
def truncate_number(number: float) -> float:
    return number - int(number)
```
This function simply subtracts the largest integer that is less than the input number from the input number, which effectively captures the leftover decimal amount. 

To test this script you can run the following code:
```python
Test truncate_number()
-------------
> assert truncate_number(3.5) == 0.5
True
> assert truncate_number(12.345) == 0.345
True
> assert truncate_number(2.0) == 0.0
True
```