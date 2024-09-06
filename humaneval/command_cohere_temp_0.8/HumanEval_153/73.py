```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The function `Strongest_Extension` takes in the class name and a list of extensions as parameters. It initializes the strongest extension found so far and its strength to negative values, initialized to the weakest possibility. The strength score is updated according to the algorithm described in the problem. The loop iterates through each extension, calculates its strength, and updates the strongest extension and its corresponding strength if the new extension is stronger. Finally, the function returns the class name appended with the strongest extension. 

The example provided in the prompt should return `Slices.SErviNGSliCes` as the strongest extension. 

This solution assumes that the extensions are valid Python identifiers, which is a reasonable assumption given the problem statement.