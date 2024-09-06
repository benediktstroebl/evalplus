```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap_count = sum(char.isupper() for char in extension)
        sm_count = sum(char.islower() for char in extension)
        strength = cap_count - sm_count
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'
```

The script uses a simple algorithmic solution. It first finds the strongest extension by calculating the strength of each extension as the difference between the number of uppercase letters and the number of lowercase letters. The strongest extension is selected by choosing the one with the greatest strength and its index is stored in the `strongest_index` variable. 

The strongest extension is then returned in the format ClassName.StrongestExtension by using the `strongest_index` to access the strongest extension in the `extensions` list. If there are two or more extensions with the same strength, it is ensured that the one returned is the one that comes first in the list by indexing with `strongest_index`. 

The code is self-contained and can be executed directly to test it. You can print the output of the `Strongest_Extension` function for any input by calling the function with the input values and capturing the output.