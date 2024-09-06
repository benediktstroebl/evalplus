```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, e
    return f'{class_name}.{strongest}'
```

The function uses two variables, `strongest` and `strength`, to record the extension with the strongest strength and the value of its strength, respectively. The sum of `cap` and `sm` gives the total number of characters in the extension.

The loop iterates through each extension in `extensions`, calculates its strength, and updates `strongest` and `strength` if it finds an extension with a stronger strength. After the loop completes, `strongest` and `strength` will store the strongest extension and its strength, respectively.

Finally, the function returns the formatted result string, which tells the caller which class name and strongest extension to use, e.g., `class_name.strongest_extension`. 

This solution adheres to the problem's guidelines, as it chooses the strongest extension and breaks ties by choosing the extension that appears first in the list.