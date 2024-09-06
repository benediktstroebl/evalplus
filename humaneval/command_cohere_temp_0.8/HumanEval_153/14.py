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

The function uses two variables, `strongest` and `found`, to keep track of the strongest extension found so far and the index of the strongest extension in the list of extensions, respectively. The function then iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase letters and the number of lowercase letters in the extension. If the strength of the current extension is greater than the strength of the current strongest extension, or if the strength is equal but the extension appears earlier in the list, the variables `strongest` and `found` are updated.

Finally, the function returns the string `class_name.strongest_extension`, where `strongest_extension` is the strongest extension found, or the extension with the same strength that appears earliest in the list.