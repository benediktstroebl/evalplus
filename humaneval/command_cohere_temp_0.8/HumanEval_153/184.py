```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f"{class_name}.{strongest_name}"
```

The function calculates the strength of each extension by subtracting the number of lowercase letters from the number of uppercase letters in the name. If there are two or more extensions with the same strength, it chooses the one that comes first in the list. The function then returns the class name combined with the strongest extension name.

Here is an example of usage:
```python
print(Strongest_Extension("Slices", ["SERviNGSliCes", "Cheese", "StufFed"]))
```

Which should print:
```
Slices.SERviNGSliCes
``` 

This is due to 'SERviNGSliCes' having the strongest strength of -1, among other parameters.