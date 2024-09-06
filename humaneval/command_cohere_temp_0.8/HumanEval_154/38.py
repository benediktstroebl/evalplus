```python
def cycpattern_check(first, second):
    return second in set(rotations(first))

def rotations(string):
    rotations = [string[i:j] for i in range(len(string)) for j in range(i, len(string))]
    return rotations
```