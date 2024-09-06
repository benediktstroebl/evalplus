```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function uses two variables, `strongest` and `found`, to keep track of the strongest extension found so far and its position in the list. It then iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters, and updates `strongest` and `found` if it finds an extension with greater strength. Finally, it returns the strongest extension appended to the class name.