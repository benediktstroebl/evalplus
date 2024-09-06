```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of a number x to base b.
    x = int(input())
    base = int(input())
    if x < 0 or base < 2:
        raise ValueError("Invalid base value.")
    result = [pow(x, (i + 1) / base) for i in range(base)]
    return str(result)

x8 = 8
x2 = 2
try:
    print(change_base(x8, 2))
except ValueError as e:
    print(e)
try:
    print(change_base(x2, 8))
except ValueError as e:
    print(e)
try:
    print(change_base(-7, 2))
except ValueError as e:
    print(e)
```