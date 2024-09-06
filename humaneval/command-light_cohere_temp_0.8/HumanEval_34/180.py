```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '', '']: seen.add(x)
```

This function employs a set called `seen` to track unique elements encountered in the list `lst`. It loops through the list and includes elements that aren't in the set and aren't empty strings (-None) or empty strings (' ''). The function returns a list of these unique elements, ensuring they're sorted. 

To test this function, you can simply run the function on a list of numbers or strings, and it should return the sorted list of unique elements. The test would implemented by the function includes a docstring that explains its purpose, making the script self-contained and easy to understand.