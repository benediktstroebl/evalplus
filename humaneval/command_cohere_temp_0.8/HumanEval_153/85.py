```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, ext
    return f'{class_name}.{strongest}'
```

The function iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is greater than the current strongest extension, the strongest extension and its strength are updated.

The final output returns the class name combined with the strongest extension name, resulting in a string in the format 'ClassName.StrongestExtensionName'. 

This approach ensures that stronger extensions with higher positive differences between uppercase and lowercase letters are favored, and in cases of tie, it returns the extension name that appears first in the list.