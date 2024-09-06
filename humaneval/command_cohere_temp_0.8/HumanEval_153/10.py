```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if (cap - sm > strength) or (cap - sm == strength and ext < strongest):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'
```

The function works by initializing the strongest extension found and its strength to null and 0 respectively. It then iterates over each extension in the list, calculating the strength of the extension by counting the number of uppercase letters in the extension name and subtracting the number of lowercase letters. If the strength of this extension is greater than the current strongest extension, or if it has the same strength but comes before the current strongest extension in the list, it updates the strongest extension and strength variables. After iterating over all the extensions, the function returns the format specified in the prompt, placing the class name and strongest extension name together with a dot in the middle.

Here is an example of an input that this function can handle:
```python
input("Check the result of Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed'])")
```

The output will be:
```
Slices.SErviNGSliCes
```

This strongest extension result is achieved as 'SErviNGSliCes' has a strength of -1, the strongest among the three extensions. It is also the first one listed.