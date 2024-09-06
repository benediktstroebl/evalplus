```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

The function unique takes a list l as input and returns a sorted list of unique elements. To do this, it utilizes a set seen to keep track of elements already encountered. The list comprehension filters out elements x in l if either x is not in seen or seen.add(x) indicates that x has been added to seen and hence is a unique element, casting the element to a set via seen.add(x) before adding it ensures uniqueness regardless of the data type of x. Finally, the result list is sorted, which could be achieved via the sorted() function, and returned.

Here is an example usage of the function:
```python
>>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
[0, 2, 3, 5, 9, 123]
```

The expected result is [0, 2, 3, 5, 9, 123] and the function unique returns the list of sorted unique elements in the input list.