```python
def truncate_number(n):
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return:
    decimal part of the number
    """
    #Decompose number into integer part and fractional part
    whole = n//10
    decimals = 10*((n%10) - ((n%100)//10))
    return round(whole+decimals)
```
Do you need any other assistance with anything else?