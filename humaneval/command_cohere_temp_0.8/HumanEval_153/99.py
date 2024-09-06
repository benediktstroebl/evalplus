```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if strength < 0 or (cap - sm > strength):
            strength, strongest = cap - sm, ext
    return f'{class_name}.{strongest}'
```

The function loops through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters. If the strength of the current extension is higher or equal to the current strongest extension, the variables are updated. Finally, the function returns the string containing the class name and the strongest extension name.