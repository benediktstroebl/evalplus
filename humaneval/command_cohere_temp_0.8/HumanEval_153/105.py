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

The script follows a straightforward approach. The `Strongest_Extension` function takes in the class name and a list of extensions as inputs. It initially sets the `strongest` extension and its strength to `-1`, which signifies that no extension has been selected yet.

The function then iterates through each extension in the provided list. For each extension, it calculates two sums: `cap` for the number of uppercase letters and `sm` for the number of lowercase letters in the extension name.

Next, it calculates the strength of the current extension by subtracting `sm` from `cap`. This gives a positive value if the name has more uppercase letters than lowercase, indicating a stronger extension.

If the calculated strength is greater than the current strongest strength, the function updates the strongest extension and its corresponding strength to the current extension. This process ensures that the strongest extension is selected and tracked.

Finally, the function returns the formatted result in the required string format, `'ClassName.StrongestExtensionName'`, using the class name and the strongest extension found.

This approach efficiently solves the problem by calculating the strength of each extension and selecting the strongest one based on the defined criteria.