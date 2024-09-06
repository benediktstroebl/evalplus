```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The script calculates the strength of an extension by counting the number of uppercase letters in the extension name and subtracting the number of lowercase letters. The strongest extension is selected by comparing the strength values, and the first strongest extension in the list is chosen in case of ties. The function then returns the class name combined with the strongest extension name.