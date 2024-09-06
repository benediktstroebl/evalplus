```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The script uses a for loop to iterate through each extension in the `extensions` list. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) using summations. It computes the strength of the extension as the difference between `cap` and `sm`, and if this strength is greater than the current strongest extension, it updates the strongest extension and its corresponding name. After processing all extensions, the function returns the class name combined with the strongest extension name.

Here is a simpler solution that solves the problem by using a dictionary to rank the extensions:
```python
def Strongest_Extension(class_name, extensions):
    extension_ranks = {extension: (cap - sm) for extension, (cap, sm) in enumerate(zip(*[iter(extension.upper()) for extension in extensions]), 1)}
    return f'{class_name}.{max(extensions, key=extension_ranks.get)}'
```

This solution leverages a dictionary, `extension_ranks`, to associate extensions with their respective strengths calculated as the difference between the number of uppercase and lowercase letters. Utilizing the `enumerate` function, each extension is assigned a rank proportional to their strength, with higher values representing stronger extensions. In the event of a tie in strength, the algorithm selects the extension that appears first in the input list. Ultimately, the function returns the class name concatenated with the strongest extension name.