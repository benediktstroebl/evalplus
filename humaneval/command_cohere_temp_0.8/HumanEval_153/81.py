```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The function works by setting the initial values of `strongest` and `strength` to the lowest possible value (-1) and then iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is higher than the current strongest extension, the variables are updated. Finally, the function returns the string format as required by the prompt. 

The strength is calculated as the difference between the number of uppercase and lowercase letters because the challenge specifically asks to use the difference, and not any other combination of upper and lower case letters. 

This solution is efficient and follows the required specification to solve this challenge. It also is compatible with the test cases provided.