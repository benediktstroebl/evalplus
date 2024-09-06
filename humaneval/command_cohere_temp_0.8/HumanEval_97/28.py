```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function `multiply(a, b)` takes two integers `a` and `b` as arguments. It extracts the last digit of each number by accessing the last index of their string representations using `str(a)[-1]` and `str(b)[-1]`. These are converted back to integers using `int()` to perform the multiplication, thereby returning the product of their unit digits. 

Let's take some examples to test the functionality further:
1. `multiply(7, 5)` -> '35' (Returned Product: 5)
2. `multiply(148, 412)` -> '616' (Returned Product: 6)
3. `multiply(19, 28)` -> '528' (Returned Product: 52)
4. `multiply(2020, 1851)` -> '0' (Returned Product: 0)
5. `multiply(14, -15)` -> '300' (Returned Product: 30)