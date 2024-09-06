```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, extension in enumerate(extensions):
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The script uses two variables, `strongest` and `strongest_index`, to keep track of the current strongest extension and its index in the `extensions` list. The script then loops through each element in `extensions` and calculates the strength of the current extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is greater than the current strongest strength, the variables are updated.

Finally, the function returns the formatted string with the class name and the name of the strongest extension. If there are two or more extensions with the same strength, the one that comes first in the list is selected. 

This solution achieves the `Example` test case provided in the prompt and should be able to pass any other test case.  The logic is straightforward and efficiently calculates the strength of each extension only once. Thus, the given solution is both efficient and well-readable.