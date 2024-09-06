```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, ext
    return f'{class_name}.{strongest_name}'
```

The function uses two variables, `strongest` and `strongest_name`, which are initialized to `-1` and an empty string respectively. These variables will store the strongest extension's strength, and its name. The function goes through each extension in `extensions`, calculating the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) using summations. The strength of the extension is calculated as `cap - sm`.

If the calculated strength is greater than the current strongest strength (`strongest`), the `strongest` and `strongest_name` are updated to the current extension's strength and name. After processing all extensions, the function returns the formatted string `'class_name.strongest_name'` indicating the strongest extension added to the `class_name`. 

The expected strongest extension is returned, taking into account the strength calculation and prioritizing the first extension with the same strength.