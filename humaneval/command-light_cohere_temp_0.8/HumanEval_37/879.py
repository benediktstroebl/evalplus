```python
def sort_even(l: list):
    """Sorts a list of numbers such that all even numbers stay the same, 
    and the odd numbers are moved to the front of the list"""
    l[:::2] = [x for x in l if x%2==0]
    l[1::2] = [x for x in l if x%2!=0]
    return l

# Test function
def test_sort_even():
    test_list = [5, 6, 3, 4]
    assert sort_even(test_list) == [3, 6, 5, 4]
```