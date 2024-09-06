```python
def sort_third(l: list):
    """Sorts the list l such that all numbers not divisible by three are at the beginning, and numbers divisible by three are at the end"""
    return sorted(l, key=lambda x: not_divisible(x) and x != l[0]) where not_divisible is a function that returns True if an integer is not divisible by 3.

The following markdown code block shows how to use the function:
```python
# Sort a list in a markdown code block
Sort your list [1, 2, 3] as if it were a list of numbers not divisible by three.
```