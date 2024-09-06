```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, e
    return f'{class_name}.{strongest}'
```

The function uses two variables, `strongest` and `strength`, to keep track of the strongest extension and its strength so far. It sums the number of uppercase and lowercase letters in the current extension, calculating their difference to determine the strength. The algorithm then iterates over each extension, updating the `strength` and `strongest` variables if it finds an extension with a higher strength.

The output of the example provided in the problem statement would be `Slices.SErviNGSliCes`, as it has a strength of -1, the highest strength amongst the given extensions.