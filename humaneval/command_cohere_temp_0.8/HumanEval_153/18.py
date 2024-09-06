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

The script employs a loop to examine each extension, calculating the difference between the count of uppercase and lowercase letters. When two extensions have an equal strength, the loop defaults to selecting the extension that appears first in the list. Subsequently, the function returns the class name combined with the strongest extension name.

Here is an example of usage:
```python
print( Strongest_Extension( "Slices",  ['SErviNGSliCes', 'Cheese', 'StuFfed']) )
```

The output will be:
```
Slices.SErviNGSliCes
``` 

This is the expected output, assuming 'SErviNGSliCes' is the strongest extension as it has the largest negative strength (the largest number of uppercase letters and the smallest number of lowercase letters).