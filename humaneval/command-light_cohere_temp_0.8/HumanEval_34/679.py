```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, '']]
    # tests passed, should be good
```