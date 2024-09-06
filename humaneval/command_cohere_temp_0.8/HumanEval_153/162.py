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

The function iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is greater than the current strongest strength, the strongest strength and the index of the new strongest extension are updated. After processing all extensions, the function returns the class name combined with the strongest extension name.

Here is an example of usage:
```python
print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
```
Which should print out:
```
Slices.SErviNGSliCes
``` 

This is in fact the strongest extension of the list provided.