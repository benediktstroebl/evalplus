```python
def sort_third(l: list):
    """Sorts a list l such that all numbers divisible by three appear first"""
    l = [x for x in l if x % 3 == 0] + [x for x in l if x % 3 != 0]
    return sorted(l)
# Examples
# [1,2,3] -> [1,2,3]
# [5,6,3,4,8,9,2] -> [2,6,3,4,8,9,5]
```