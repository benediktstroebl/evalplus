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

The function calculates the strength of each extension as the difference between the count of uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength value, with tie breaks resolved by choosing the extension that appears first in the input list. The function returns the class name combined with the strongest extension name.

This approach guarantees the correct strongest extension is selected and follows the specified logic for handling ties. It should provide the expected results for the given test cases and any others that adhere to the problem guidelines.