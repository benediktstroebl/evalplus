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

The function uses two variables, `strongest` and `strongest_name`, which are initialized to `-1 and ''`, respectively. These variables will keep track of the strongest extension found, and the name of the strongest extension found, as we loop over each potential extension. The sum of `c.isupper()` will count the number of uppercase letters in the name, adding 1 for each uppercase letter, while the sum of `c.islower()` will count the number of lowercase letters, adding 1 for each lowercase letter. The difference between the two sums will be the strength of the extension, with higher positive values being stronger. Each time a stronger extension is found, both variables are updated accordingly. Once the loop is finished and there are no more extensions to check, the function returns the string `class_name.strongest_name`, which is the name of the class with the strongest extension appended.