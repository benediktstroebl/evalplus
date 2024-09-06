```python
def change_base(x, base):
    return bin(x)[2:].rjust(len(str(x)), '0')[::-1].translate(str.maketrans('10', '01'))[0:len(str(x))] if base < 2 else map(int, str(x)) if base == 10 else chr(x + 96 - (x > 9))
```