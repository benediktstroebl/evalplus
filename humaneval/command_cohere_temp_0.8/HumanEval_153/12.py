```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        extension_strength = cap - sm
        if extension_strength > strength:
            strength, strongest = extension_strength, e
    return f'{class_name}.{strongest}'
```

The script uses two variables, `strongest` and `strength`, to keep track of the strongest extension and the strength of the current extension, respectively. The code iterates over each extension, calculating the number of capital and small letters. The strength of the extension is calculated using the difference between cap and sm, and if the calculated strength is greater than the current strength, both variables are updated. Finally, the function returns the strongest extension name concatenated with the class name.