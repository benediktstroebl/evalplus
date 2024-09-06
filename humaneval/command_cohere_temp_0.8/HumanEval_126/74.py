```python
def is_sorted(lst):
    lst.sort()   
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list and then uses a set to keep track of its unique elements. It returns 'False' if any element is encountered twice in the sorted list. Otherwise, it returns 'True'. 

This approach has a time complexity of O(n log n) due to the sorting step, but it only performs a single pass on the list, making it still quite efficient. If absolute efficiency was the goal, sorted() could be changed to a radix sort implementation to minimize the overhead of sorting. However, the given approach is both simple and efficient enough for most practical purposes. 

The tests would look like these:
```python
test_cases = [
    ([5], True),
    ([1, 2, 3, 4, 5], True),
    ([1, 3, 2, 4, 5], False),
    ([1, 2, 3, 4, 5, 6], True),
    ([1, 2, 3, 4, 5, 6, 7], True),
    ([1, 3, 2, 4, 5, 6, 7], False),
    ([1, 2, 2, 3, 3, 4], True),
    ([1, 2, 2, 2, 3, 4], False)
]

for test_case in test_cases:
    assert is_sorted(test_case[0]) == test_case[1]
```