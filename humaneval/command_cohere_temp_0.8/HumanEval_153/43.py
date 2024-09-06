```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function uses two nested loops to iterate through the list of extensions and calculate the strength of each extension based on the number of uppercase and lowercase letters. The strongest extension is selected by comparing the strength of each extension and updating the strongest and found variables accordingly. The function then returns the class name combined with the strongest extension.