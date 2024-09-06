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

The script calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength measure, and the function returns the corresponding class name followed by the strongest extension name. If there are ties in strength, the first occurrence in the list is selected.