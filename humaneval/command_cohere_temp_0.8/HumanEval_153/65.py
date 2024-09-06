```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between uppercase and lowercase letters in the extension name. The strongest extension is selected based on this strength value, with the tie broken by choosing the extension that appears first in the list. The function returns the class name combined with the strongest extension. 

This approach ensures that the code is efficient and can handle multiple extensions with the same strength value. 

The `strongest` and `strongest_index` variables are initialized to default values of `-1` before the loop. During each iteration of the loop, the strength of the current extension is calculated, and if it's greater than the current `strongest` value, `strongest` and `strongest_index` are updated to the new strength and the index of the current extension in the `extensions` list. 

The `enumerate` is used to access the index of each extension during the loop, and it also assigns a counter to the extension, which is just a nickname and doesn't affect the functionality of the code.  This approach simplifies the code and makes it more readable.