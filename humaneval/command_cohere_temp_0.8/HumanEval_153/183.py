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

The function loops through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. If the strength is greater than the current strongest extension, the strongest extension and its name are updated. Finally, the function returns the class name and the strongest extension name concatenated with a dot in between. The solution is self-contained as it doesn't rely on any external variables or functions and can be run independently.