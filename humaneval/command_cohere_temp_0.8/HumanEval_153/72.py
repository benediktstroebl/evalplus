```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        curr_strength = cap - sm
        if curr_strength > strength:
            strength = curr_strength
            strongest = ext
    return f'{class_name}.{strongest}'
```

The function calculates the strength of each extension by subtracting the number of lowercase letters from the number of uppercase letters in the name. The strongest extension is selected, considering the rule that in case of a tie, the extension that appears first in the list is chosen. The function then returns the class name combined with the strongest extension. 

Here is an example of usage:
```python
print(Strongest_Extension('Foo', ['A', 'B', 'C'])) # Foo.A
```

This would be the expected output, as 'A' has the strongest strength among the extensions provided.