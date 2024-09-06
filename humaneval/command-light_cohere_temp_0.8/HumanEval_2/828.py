```python
def truncate_number(n: float) -> float:
    return (n//1) if n > 1 else n
```
The function takes a number n, which can be represented as a float, and returns the decimal part of the number. It does this by checking if the number is greater than 1, and if so, it divides the number by 1. If the number is 1 or less than 1, then it returns the number as is, without changing.