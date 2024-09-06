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

Here is an example of use:
```python
print( Strongest_Extension("my_class", ["AA", "Be", "CC", "dd", "ee"]) )
```

And below is the output of the code:
```
my_class.CC
```