```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = 0, 0
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength value, with the tie broken by choosing the extension that appears first in the list. The function returns the class name combined with the strongest extension name.