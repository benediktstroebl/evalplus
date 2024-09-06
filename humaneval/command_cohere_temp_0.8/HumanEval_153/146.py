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

The script uses a simple iterative approach to calculate the strength of each extension and selects the one with the highest strength. In the event of a tie, it will return the extension that appears first in the list. The function returns the class with the strongest extension among the provided list of extensions.