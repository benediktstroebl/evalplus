```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap = sum(char.isupper() for char in extension)
        sm = sum(char.islower() for char in extension)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. The strongest extension is selected based on this strength value, with the tie broken by choosing the extension that appears first in the list. The function then returns the class name combined with the strongest extension.