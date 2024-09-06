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

The function calculates the strength of each extension by counting the number of uppercase and lowercase letters in the extension name (`cap` and `sm` respectively). The difference between these counts represents the strength of the extension. The method compares this calculated strength with the current strongest extension identified. The function will return the class with the strongest extension, as per the problem's specifications. 

The strength calculation and comparison process is conducted anew for each extension in the list. Thus, if multiple extensions share the same strength, the strongest extension is selected based on the order it appears in the input list. The function adheres to the problem's specified approach of selecting the strongest extension.