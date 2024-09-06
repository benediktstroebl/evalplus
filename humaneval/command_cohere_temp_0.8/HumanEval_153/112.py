```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        if strength < cap - sm:
            strength = cap - sm
            strongest = e
    return f'{class_name}.{strongest}'
```

The function works by initializing the strongest extension found and its strength to null and -1 respectively. It then iterates through the list of extensions and calculates the strength of each extension by counting the number of uppercase and lowercase letters in the extension name. If the strength of the current extension is greater than the current strongest extension, the strongest extension and its strength are updated. After iterating through all the extensions, the function returns the class name concatenated with the strongest extension name.

The expected output for the given example case is 'Slices.SErviNGSliCes'.