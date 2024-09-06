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

The function works by initializing the strongest extension and its strength to negative values and then loops through all extensions. It calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is greater than the current strongest extension, the strongest extension and its strength are updated. After looping through all extensions, the function returns the class name combined with the strongest extension name.

Here is an example function call:
```python
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'dd', 'ee']))
```

Which should output:
```
my_class.AA
``` 

This is due to the fact that 'AA' has the strongest strength of -1 since all letters are uppercase.