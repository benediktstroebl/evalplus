```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, e
    return f"{class_name}.{strongest_name}"
```

The function iterates over the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is selected by comparing the strength and stored in the `strongest_name` variable with the corresponding strongest name. The strongest extension is then returned in the format ClassName.StrongestExtension.