```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, ext
    return f'{class_name}.{strongest}'
```

The script employs a nested loop to effectively iterate through the `extensions` list. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) using iterative summations. By subtracting `sm` from `cap`, it determines the strength of the extension. If the current strength is higher than the strongest found thus far, the script updates the `strongest` extension and the corresponding highest strength. 

Finally, it creates and returns the desired string, formatting the class and strongest extension names neatly with a period in between (e.g., `my_class.AA`). 

This succinct and effective solution harnesses basic Python mechanics, delivering a function that powerfully embodies the problem's requirements.