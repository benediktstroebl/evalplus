```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, e
    return f'{class_name}.{strongest}'
```

The strength of the extension is determined by the difference between the number of uppercase letters and the number of lowercase letters in the extension name. The script iterates through the list of extensions, calculating the strength of each one, and selects the strongest extension among those with the same strength, choosing the first one that appears in the list. The function returns the class name combined with the strongest extension name.