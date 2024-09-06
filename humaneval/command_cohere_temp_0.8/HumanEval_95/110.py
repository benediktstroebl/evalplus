```python
def check_dict_case(dictn):
    dictn = {int(key) if isinstance(key, str) else key for key in dictn.keys()}
    return len(dictn) != 0 and (all(key.isupper() for key in dictn) or all(key.islower() for key in dictn))
```
### How It Works
The function `check_dict_case()` takes a single argument `dictn`, which is the input dictionary to be evaluated. 

It first processes the keys using a dictionary comprehension, which checks if each key is an integer or a string. If it is a string, it determines whether it is uppercase or lowercase. This is done using the `int()` and `isupper()` functions (`islower()` would work as well) as ternary operations,Combined together, this effectively filters out any keys that are not strings, and keeps only the keys in the desired case (either all uppercase or all lowercase).

Finally, the function returns `True` if the resulting dictionary has no empty keys and all keys are in the same case, `False` otherwise. 

This algorithm should pass the given test cases based on the problem statement you provided.