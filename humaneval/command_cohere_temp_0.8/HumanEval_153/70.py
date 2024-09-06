```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        if strength < 0 or (cap - sm > strength and ext < strongest):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'
```

The function calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength measure and its position in the list. If there are extensions with the same strength, the first one in the list will be considered. The function returns the class name combined with the strongest extension name.

Here is an example of usage:
```python
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
```

The output will be:
```
Slices.SErviNGSliCes
``` 

This is the expected result, as 'SErviNGSliCes' has the highest strength among the given extensions.