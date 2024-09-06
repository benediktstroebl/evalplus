```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The function works by initializing the variables `strongest` and `strength` with the lowest and weakest strength. Then, it loops through the extensions, calculating the strength of each extension with the formula `cap - sm`, and if the calculated strength is greater than the current strongest strength, the variables are updated. Lastly, the function returns the strongest extension formatted as `ClassName.StrongestExtension`.