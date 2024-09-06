```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = 0, 0
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength value, with the tie broken by choosing the extension that appears first in the list. The function returns the resulting class name and strongest extension name concatenated.

Here is an example usage of the function:
```python
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
```
The output will be:
```
Slices.SErviNGSliCes
``` 

This is in fact the strongest extension according to the given strength criteria.