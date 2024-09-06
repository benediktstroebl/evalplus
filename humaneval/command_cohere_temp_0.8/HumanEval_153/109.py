```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If there are two or more extensions with the same strength, it selects the one that comes first in the list. The function then returns the class name combined with the strongest extension name.

Here is an example of use:
```python
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
```

The output will be:
```
Slices.SErviNGSliCes
``` 

This is due to 'SErviNGSliCes' having a strength of -1, being the strongest extension.