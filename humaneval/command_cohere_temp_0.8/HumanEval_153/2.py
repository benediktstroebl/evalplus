```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function uses a simple algorithm that calculates the strength of each extension by subtracting the number of lowercase letters from the number of uppercase letters in the extension name. The extension with the highest strength is selected and its position in the list is recorded in the `found` variable. In case of a tie between multiple extensions with the highest strength, the function will return the one that appears first in the list. The function then constructs and returns the required string.