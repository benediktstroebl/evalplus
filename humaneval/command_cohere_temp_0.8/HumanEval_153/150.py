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

The script follows a simple approach to solve the problem:
1. It initializes the variables `strongest` and `strength` with default values `-1` (to track the strongest extension and its strength).
2. It iterates through each extension in the `extensions` list.
3. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) in the extension name.
4. It calculates the strength of the extension as the difference between `cap` and `sm`.
5. If the calculated strength is greater than the current strongest strength, it updates the `strength` and `strongest` variables with these new values.
6. After iterating through all extensions, the function returns the formatted string containing the class name and the strongest extension name.

The script guarantees that if there's a tie in the strength of extensions, it will return the one that appears first in the list. 

Note that this solution is optimized for readability and simplicity, assuming that the list of extensions won't be too long, as is often the case in real-world scenarios. If you were dealing with a large list, consideration would have to be given to optimizing performance.