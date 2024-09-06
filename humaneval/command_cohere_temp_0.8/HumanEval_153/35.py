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

The script employs a loop to examine each extension, calculating the difference between the count of uppercase and lowercase letters to determine their strength. When multiple extensions possess identical strength, it ensures the one encountered earliest in the list is selected. 

The `strongest, found = -1, -1` line initializes the variables `strongest` and `found` to -1 for each new examination of extensions, possibly enhancing the function's performance, albeit slightly. The script efficiently solves the problem and outputs the class with the strongest extension among those provided.