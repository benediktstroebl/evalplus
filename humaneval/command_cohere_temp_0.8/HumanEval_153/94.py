```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        strengths[e] = strength
    strongest = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest}'
```

The code works by first summing the number of uppercase letters and summing the number of lowercase letters for each extension separately. Then, it calculates the difference between the two sums, which represents the strength of each extension. Afterward, it sorts extensions by their strength in a dictionary format, with the key being the extension name and the value being its strength. Finally, it chooses the first extension among the strongest extensions with the same strength.

The strength of an extension is calculated by the difference between the number of uppercase and lowercase letters in the extension name. The strongest extension is chosen based on this strength, and if there are multiple strongest extensions, it chooses the one that appears first in the list. The function returns the class name and the strongest extension name concatenated with a dot (`.`). 

Here is an example of how to use the `Strongest_Extension()` function:
```python
# Example 1:
class_name = "MyClass"
extensions = ["AA", "Be", "CC", "aaa", "Bb", "Cc"]
result = Strongest_Extension(class_name, extensions)
print(result)  # Expected: MyClass.AA

# Example 2:
class_name = "Slices"
extensions = ["SErviNGSliCes", "Cheese", "StuFfed"]
result = Strongest_Extension(class_name, extensions)
print(result)  # Expected: Slices.SErviNGSliCes
``` 

In the examples, the `Strongest_Extension()` function would return the strongest extension for the given `class_name` and `extensions`.