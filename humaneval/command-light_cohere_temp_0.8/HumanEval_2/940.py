```python
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into 
    and integer part (largest integer smaller than given number) and decimals. 
    Return the thus the recent decimal part of the number
    """
    
    number = float(number)  # Convert number to float
    int_part = math.floor(number)
    decimals = number - int_part
    
    return decimals
```
The function `truncate_number` takes a floating point number `number: float` as an argument and returns the decimal part of the number. The function first converts the to float to ensure proper mathematical operations. Then it computes the another integer part of the number using `math.floor(number)`, which returns the largest integer less than the number. Finally, the function returns the decimal part of the number, which is the remaining value of `number` minus the `int_part` result.