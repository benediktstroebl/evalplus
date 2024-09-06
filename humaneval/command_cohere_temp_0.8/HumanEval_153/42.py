```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for ext_index, extension in enumerate(extensions):
        cap_count = sum(char.isupper() for char in extension)
        sm_count = sum(char.islower() for char in extension)
        strength = cap_count - sm_count

        # Assign the strongest extension and its index
        if strength > strongest:
            strongest, strongest_index = strength, ext_index

    # Return the result
    return f'{class_name}.{extensions[strongest_index]}'
```

The script calculates the strength of each extension as the difference between uppercase and lowercase letter counts in the extension name. The strongest extension is selected and remembered in a variable along with its index. If there's a tie in strength, the extension that comes first in the list is chosen. The function returns the class name combined with the strongest extension name.