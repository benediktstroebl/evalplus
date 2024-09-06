```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The function works by initializing the strongest extension and its strength to negative values. It then iterates through the list of extensions and calculates the strength of each extension by counting the number of uppercase and lowercase letters. If the calculated strength is greater than the current strongest extension, the strongest extension and its strength are updated. Finally, the function returns the class name appended with the strongest extension.