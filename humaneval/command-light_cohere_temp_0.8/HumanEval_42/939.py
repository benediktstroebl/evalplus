```python
def incr_list(lst):
    n = len(lst)
    result = [0] * (n + 1)
    for i in range(n):
        result[i+1] = lst[i] + 1
    return result

# Test
def test_incr_list():
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    assert list(incr_list(lst)) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Run tests and print results
test_incr_list()
print("Tests passed!")
```