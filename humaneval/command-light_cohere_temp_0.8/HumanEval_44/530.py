```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base base.
    Returns a time string representation of x after the conversion.
    """
    formats:
    - If base is 10, it returns '101010' for 120.
    - If returns the different base numbers.
    """
    using base conversion rules:
    10^9 -> 100000000
    10^8 -> 1000
    10^6 -> 10000
    10^4 -> 100000
    10^3 -> 10000
    10^2 -> 100
    10 -> 101
    """
    return f"{x:10}{base}"

x = int(123)
y = change_base(x, 10)
print(y)
```