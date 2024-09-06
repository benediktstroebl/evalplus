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

The script calculates the difference between the number of uppercase and lowercase letters in the name of each extension. This difference represents the strength of each extension. The strongest extension is chosen from the list of extensions based on this strength measure and its position in the list (in case of a tie). The function returns the class name combined with the strongest extension name.