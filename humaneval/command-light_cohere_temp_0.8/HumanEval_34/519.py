```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and not item!isin_set]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This code defines a function `unique` that returns a list of unique elements from the input list `lst`. The `test_unique` function tests the `unique` function with an example list and asserts the expected output, checking for correctness.