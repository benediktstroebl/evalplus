```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        cur_strength = cap - sm
        strengths[ext] = cur_strength
    
    strongest = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest}'
```

The code calculates the strength of each extension using the formula of difference between uppercase and lowercase letters, and assigns the strongest extension to the `strongest` variable. In case of a tie, it selects the extension that appears first in the list. The final output is formatted as `ClassName.StrongestExtension`.