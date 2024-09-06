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

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. The strongest extension is selected based on this strength value, choosing the first one if there are multiple extensions with the same strength. The function then returns the class name combined with the strongest extension name.