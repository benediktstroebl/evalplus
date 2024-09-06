```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, e
    return f'{class_name}.{strongest_name}'
```

The script uses a simple algorithmic solution with a loop through each extension, calculating its strength, and picking the strongest one. If there are ties, it will select the extension that appears first in the list.

The solution follows the spec quite closely, using no external libraries for filtering out strengths and applying ties logic with list indexing. It achieves this without using any list slicing, opting instead for a `for` loop.