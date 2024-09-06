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

The script employs a loop to examine each extension, assessing the strength of each by calculating the difference between the count of uppercase and lowercase letters. If the strength is higher than the current strongest or, in the event of a tie, if the extension's sequence index is smaller than that of the current strongest, the variables for the strongest and found indices are updated. Finally, it returns the class name combined with the strongest extension.

The implementation excels in both efficiency and readability, promptly responding to alterations in the size of the input list or the structure of the extensions.