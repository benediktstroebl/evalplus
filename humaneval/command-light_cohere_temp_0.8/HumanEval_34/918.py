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
    list1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = unique(list1)
    assert len(result) == 7
    assert set(result) == set([0, 2, 3, 5, 9, 123])
    assert sorted(result) == [0, 2, 3, 5, 9, 123]

# Run the function and test
unique(test_unique())
 ```