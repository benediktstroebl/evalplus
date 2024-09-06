```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        # Assign the strongest extension
        if strength > strongest:
            strongest, strongest_index = strength, index

    # Return the strongest extension name
    return f'{class_name}.{extensions[strongest_index]}'
```

The script uses a simple algorithm to find the strongest extension. It calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. The extension with the highest strength is stored in the strongest variable along with its index in the extensions list. If there are two or more extensions with the same strength, the algorithm selects the one that comes first in the list. The function then returns the class name combined with the strongest extension name.