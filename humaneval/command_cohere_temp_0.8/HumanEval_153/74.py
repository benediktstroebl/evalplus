```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        if strength < 0 or (cap - sm > strength and strength != -1):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'
```

The function goes through each extension, calculating the difference between the number of uppercase and lowercase letters. The strongest extension is the one that yields the highest difference, or the one with the highest strength when the strength is tied among multiple extensions. The function then returns the class name combined with the strongest extension.