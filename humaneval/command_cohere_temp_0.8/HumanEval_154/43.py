```python
def cycpattern_check(a, b):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    a = a.lower()
    b = b.lower()
    b = b.replace(" ","")
    b = b.strip(".")
    b = b.strip("!")
    b = b.strip("?")
    b = b.strip(",")
    b = b.strip("'")
    return (a.find(b) >= 0) or any(a.find( rotated_b ) >= 0 for rotated_b in rotated_b_generator(b))

def rotated_b_generator(b):
    """
    Generate all rotations of a given string.
    """
    # quarter rotation
    quarter_rot = lambda x: x[1:] + x[0:1]
    # half rotation
    half_rot = lambda x: x[1:][::-1] + x[0:1][::-1]
    yield b
    yield quarter_rot(b)
    yield half_rot(b)
    yield b[::-1]
    yield quarter_rot(b[::-1])
    yield half_rot(b[::-1])
```