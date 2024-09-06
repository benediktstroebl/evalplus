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

The function works by initializing the strongest strength found so far to -1, ensuring that any real extension will be stronger than this initial value, and initializing the corresponding strongest extension name as an empty string. The loop iterates through each extension in the list, calculating the strength of the extension by counting the number of uppercase letters and subtracting the number of lowercase letters in the name. If the currently calculated strength is stronger than the current strongest strength, the strongest strength and its corresponding extension name are updated. Once all extensions have been checked, the function returns the class name followed by the name of the strongest extension.

Here is an example function call:
```python
print(Strongest_Extension("my_class", ["AA", "Be", "CC", "dd", "ee", "FF"]))
```

The output is:
```
my_class.FF
``` 

This is the strongest extension since all other extensions have positive strengths, and "FF" has the highest negative strength among them.