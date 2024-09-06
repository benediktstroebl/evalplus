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

The function iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is greater than the current strongest strength or is equal and the extension appears earlier in the list than the current strongest extension, the strongest extension and its index are updated. Finally, the function returns the class name concatenated with the strongest extension name.