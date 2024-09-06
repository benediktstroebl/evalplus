```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. The strongest extension is selected, and if there are ties, it picks the one that appears first in the list. The function then returns the class name combined with the strongest extension. 

The markdown code block above contains a Python script with a function named `Strongest_Extension` that solves the problem described in the statement. This function takes in two parameters: `class_name`, which is a string representing the name of the class, and `extensions`, which is a list of strings representing the available extensions for the class. The function calculates the strength of each extension by counting the number of uppercase letters and lowercase letters in each extension's name. The strength is calculated as the difference between the number of uppercase letters and the number of lowercase letters. The function then compares the strengths of all the extensions and selects the strongest one. If there's a tie, the function will choose the extension that comes first in the list. Finally, the function returns a string that combines the class name with the strongest extension, separated by a dot.