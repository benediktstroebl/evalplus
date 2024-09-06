```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        ext_strength = cap - sm
        if ext_strength > strength:
            strength, strongest = ext_strength, e
    return f'{class_name}.{strongest}'
```

The function uses two variables, `strongest` and `strength`, which keep track of the strongest extension and its strength so far, initially assuming no extension is stronger than another. The function then loops through each extension, calculating its strength as the difference between the number of uppercase and lowercase letters, and if the strength is greater than the current strongest extension, updates the `strength` and `strongest` variables.

Finally, the function returns the string formatted with the class name and the strongest extension name. 

Note: This solution assumes that the list of extensions passed in is valid, including proper string formatting and excluding any null values.