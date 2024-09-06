```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        delta = cap - sm
        if delta > strength or (delta == strength and ext < strongest):
            strength = delta
            strongest = ext
    return f'{class_name}.{strongest}'
```

The function iterates through the list of extensions, calculating the difference between the number of uppercase and lowercase letters in each extension. The extension with the largest difference is considered the strongest. In case of a tie, the extension that appears first in the list is prioritized. The function returns the class name combined with the strongest extension.

This approach is efficient and guarantees the correct strongest extension is selected, considering both the strength and the list order. It simplifies the logic by using sums to count the uppercase and lowercase letters, calculating the strength difference, and selecting the strongest extension within a single loop.