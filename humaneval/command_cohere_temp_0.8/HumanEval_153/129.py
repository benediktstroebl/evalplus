```python
def Strongest_Extension(class_name, extensions):
    strongest, found = -1, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function examines each extension, calculating the difference between the count of uppercase and lowercase letters. The strongest extension is selected if its strength is greater than the previous one, or it has the same strength but appears earlier in the list. The function then returns the class name combined with the strongest extension.

This solution adheres to the problem's guidelines, choosing the strongest extension based on the letter count difference and prioritizing ties by their order in the list.