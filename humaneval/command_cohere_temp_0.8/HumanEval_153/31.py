```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, extension in enumerate(extensions):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest = strength
            strongest_index = i
    return f'{class_name}.{extensions[strongest_index]}'
```

The script calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the names of the extensions. The strongest extension is selected with the highest strength, and if there are ties, it selects the one that appears first in the list. The selected extension is then formatted with the class name and the strongest extension name and returned.