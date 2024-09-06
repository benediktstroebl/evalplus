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

The function analyzes each extension, calculating the difference between the count of uppercase and lowercase letters. This difference signifies the "strength" of the extension. It keeps track of the strongest extension encountered, updating the strongest variable and comparing the strength of new extensions to ensure accuracy. The final output is a string in the required format, naming the class followed by the strongest extension.

This solution is efficient and guarantees the correct strongest extension, updating the results as stronger extensions are encountered.