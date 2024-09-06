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

The script calculates the strength of each extension using the equation `cap - sm`, where `cap` is the number of uppercase letters and `sm` is the number of lowercase letters. The strongest extension is selected by comparing the strength values, and the first strongest extension in the list is chosen if there is a tie. The final output is returned in the format `ClassName.StrongestExtensionName`.