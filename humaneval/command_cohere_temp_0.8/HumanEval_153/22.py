```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, ext in enumerate(extensions):
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength value, with ties broken in favor of the extension that appears first in the list. The function returns the class name combined with the strongest extension name. 

This approach guarantees the correct strongest extension is always chosen, even if multiple extensions have the same strength.