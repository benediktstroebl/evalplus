```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is higher than the current strongest strength or is equal but the current extension appears earlier in the list than the one associated with the current strongest strength, the strongest strength and its corresponding index are updated. Finally, the function returns the strongest extension name concatenated with the class name.