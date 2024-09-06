```python
def truncate_number(n: float) -> float:
    return n // 10 if n >= 10 else n

n = truncate_number(15)
# Result is guaranteed by definition of the function

n = truncate_number(3.5)
# Result is not 15.4, but the integer part is 3 and decimal part is 0.1.

n = truncate_number(0.5)
# Result is not 5, but 0.4

n = truncate_number(-33.5)
# Result is not an integer, but -34.5

```