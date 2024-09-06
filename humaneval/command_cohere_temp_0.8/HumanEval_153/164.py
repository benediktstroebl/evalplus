```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, e
    return f'{class_name}.{strongest_name}'
```

The function analyzes each extension, calculating the difference between the number of uppercase and lowercase letters. The strongest extension is chosen if its difference is greater than the previous strongest. The final output follows the format of `class_name.strongest_extension_name`. This approach ensures that stronger extensions override weaker ones, even if their order differs in the list.

The code has a time complexity of `O(n)` and a space complexity of `O(1)`, making it an efficient solution for this class strengthening task.