```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f"{class_name}.{strongest_name}"
```

The function calculates the strength of each extension by subtracting the number of lowercase letters from the number of uppercase letters in the name. The strongest extension is selected, considering the case when two or more extensions have the same strength. The selected strongest extension is then returned in the format `ClassName.StrongestExtensionName`.