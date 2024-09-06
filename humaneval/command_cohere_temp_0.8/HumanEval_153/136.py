```python
def Strongest_Extension(class_name, extensions):
    strongest, found = -1, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is selected, considering both strength and alphabetical order in case of ties. The function then returns the class name combined with the strongest extension name.