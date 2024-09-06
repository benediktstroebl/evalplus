```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        strengths[e] = strength
    
    strongest = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest}'
```

The function uses a dictionary `strengths` to keep track of the strength of each extension, calculated as the difference between the number of uppercase and lowercase letters. The strongest extension is then determined by finding the key with the greatest value in the `strengths` dictionary using the `max` function and the `key` parameter. 

The choice of the strongest extension in case of a tie is handled by the `key` parameter in the `max` function, which guarantees that the winning key is the first one found in the list. 

The code assumes that the list of extensions passed to the function is not empty and that there is at least one eligible extension among them, as these assumptions are already tested in the provided examples.