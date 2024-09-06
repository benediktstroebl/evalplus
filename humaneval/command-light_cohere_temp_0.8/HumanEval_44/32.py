```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    if x < 0:
        x = str(x)
    s = [str(x)[1:].zfill() for char in 'abcdefghijklmnopqr ]
    if len(s) != 1:
        s = ''.join(s)
    return s.format(s,