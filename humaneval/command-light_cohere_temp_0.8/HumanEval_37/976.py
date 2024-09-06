```python
def sort_even(lst):
    even = []
    for x in lst:
        if x % 2 == 0:
            even.append(x
    elif x != 0:
            pass
    even.sort()
   
    return even
def test_sort_even(test_list):
    expected = [2, 3]
    got = test_list
    assert expected == got, "Failed test: " + str(expected) + " != " + str(got)
    return got
```