```python
def truncate_number(n: float) -> float:
    return n if not n.is_integer() else n //__int__() // (n - 1)
```
The function first checks if the input is an integer, and if so, it returns the integer. If the input is not an number, it converts it to an integer and then divides it by (n - 1) to truncate the decimal part.