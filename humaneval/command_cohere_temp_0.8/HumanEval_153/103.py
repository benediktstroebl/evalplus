```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if strength < 0 or (cap - sm > strength):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'
```

The function calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength measure, and the function returns the corresponding class name followed by the strongest extension. If multiple extensions have the same strength, the first one encountered in the list is selected.