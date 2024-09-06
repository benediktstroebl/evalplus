```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        ext_strength = cap - sm
        if ext_strength > strength:
            strength, strongest = ext_strength, e
    return f'{class_name}.{strongest}'
```

The script uses a simple loop to iterate through the list of extensions. For each extension, it counts the number of uppercase and lowercase letters. The strength of the extension is calculated as the difference between these two counts. If the calculated strength is greater than the current strongest extension, the strongest extension and its strength are updated. Finally, the function returns the strongest extension name concatenated with the class name.