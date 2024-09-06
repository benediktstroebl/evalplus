```python
def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    strongest_strength = 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest = ext
            strongest_strength = strength
    return f'{class_name}.{strongest}'
```

The script uses a simple brute-force approach. It first assumes the first extension in the list is the strongest one and sets its strength to 0. Then, it loops over all other extensions, calculating the strength of each one, and if the strength is greater than the one of the current strongest extension, the strongest extension is updated. 

The strength is calculated simply by summing the number of uppercase letters in the extension and subtracting the number of lowercase letters.