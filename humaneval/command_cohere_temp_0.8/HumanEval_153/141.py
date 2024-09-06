```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, ext
    return f'{class_name}.{strongest}'
```

The strength of the extension is determined by the difference between the number of uppercase letters and the number of lowercase letters in the extension name. The function will then choose the strongest extension and return the class name followed by the strongest extension name. In the event of a tie, it will default to choosing the extension that appears first in the list. 

Let's break down the code:
1. `strongest, strength = None, -1`: Initializes two variables, `strongest` and `strength`. `None` signifies that no strongest has been set yet, and `-1` represents the highest strength possible (when the number of uppercase letters is equal to the number of lowercase letters). 
2. `for ext in extensions:`: Iterates through each extension in the list.
3. `cap = sum(1 for c in ext if c.isupper())`: Counts the number of uppercase letters in the current extension.
4. `sm = sum(1 for c in ext if c.islowser())`: Counts the number of lowercase letters in the current extension.
5. `curr_strength = cap - sm`: Calculates the current strength of the extension based on the difference between the counts.
6. `if curr_strength > strength:`: Checks if the current strength is greater than the current strongest strength found.
7. `strength, strongest = curr_strength, ext`: Updates the strongest and strength variables if the current extension is stronger.

Finally, the function returns the string formatted with the class name and the strongest extension. 

This algorithm is designed to calculate the strength of each extension in a consistent manner and provide the strongest extension based on the provided criteria.