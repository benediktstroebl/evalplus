```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected, and if there are ties, it picks the one that comes first in the list. The final output is returned as a string in the format `ClassName.StrongestExtensionName`.