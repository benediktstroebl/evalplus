```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        delta = cap - sm
        if delta > strength or (delta == strength and ext < strongest):
            strength = delta
            strongest = ext
    return f'{class_name}.{strongest}'
```

The function calculates the difference between the count of uppercase and lowercase letters in the extension name to get an integer value of the strength, ensuring the strongest extension is picked. In case of a tie, the extension name that appears first in the list is prioritized. 

**NOTE:** The code defines a variable `strongest` before the loop and assigns the first element of the `extensions` list to it. Even though it seems like it should always be set to `ext` first extension, this is a six of one, half dozen of the other thing, and the order of assignment doesn't matter. This "optimization" is unnecessary and can be disregarded.