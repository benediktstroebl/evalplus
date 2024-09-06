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

The script follows a straightforward approach. The strongest extension is initially determined by calculating the difference between the count of uppercase and lowercase letters. The strongest extension is selected and subsequently returned. In the event of a tie in terms of strength, the extension that comes first in the list is chosen. 

This solution adheres to the problem's guidelines and is structured to effectively tackle the presented problem. You can verify the functionality of the script by calling the function with example test cases.  Unlike the previous solution, this solution does not rely on converting the class name and extensions to strings. Instead, it performs the calculations directly on the provided parameters, which can save unnecessary string conversions and provide a more efficient implementation.