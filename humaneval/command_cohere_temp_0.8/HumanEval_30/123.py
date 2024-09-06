```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The algorithm uses a list comprehension, which is a common Python idiom for filtering lists based on certain conditions. 

To achieve this, the function employs a conditional statement `x > 0` in the list comprehension, which filters only those elements `x` that are greater than zero. The function returns the resulting list, which contains only the positive numbers from the input list. 

The function is designed to be self-contained, meaning it does not rely on any external variables or functions. Therefore, it is standalone and can be easily imported and used in other Python scripts, reproducing the behavior presented in the Markdown code block you provided.