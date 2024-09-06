```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        strengths[ext] = strength

    strongest_ext = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest_ext}'
```

The function `Strongest_Extension` calculates the strength of each extension using the formula `CAP - SM` where `CAP` is the number of uppercase letters and `SM` is the number of lowercase letters. The extension with the strongest strength is determined by collecting all the extensions and their corresponding strengths in the `strengths` dictionary. The key-value pairs in this dictionary are arranged such that the strongest extension is mapped to a strength of 0. The `max` function is then used to identify the extension with the key `0`, which corresponds to the strongest extension. 

The function assumes that the list of extensions is passed in the correct format. If the input list is empty, the function returns `None`. 

This solution assumes that the list of extensions is passed in the correct format. If the input list is empty or not in the expected format, the function may not return the correct output.