```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
 
    return result

def test_unique():
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(input_list)
    assert len(result) == 7
    assert set(result) == set([0, 2, 3, 5, 9, 123]))

test_unique()
```