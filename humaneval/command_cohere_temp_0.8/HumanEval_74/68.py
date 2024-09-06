```python
def total_match(lst1, lst2):
    total1 = sum(len(x) for x in lst1)
    total2 = sum(len(x) for x in lst2)
    if total1 > total2:
        return lst2
    elif total2 > total1:
        return lst1
    else:
        return lst1 if len(lst1) < len(lst2) else lst2
```

The code sums the lengths of all strings in both lists, compares the totals, and directly returns the more concise list; if the totals are the same, it returns the first list per the "if-elsei" syntax. As mentioned, this algorithm has a time complexity of O(n^2) due to repeated list traversals.

The unit tests that can be used to validate the functionality of the code are:
```python
test_list = [
    ([], []),
    ('["hi", "admin"], ["hI", "Hi"]'),
    ('["hi", "admin"], ["hi", "hi", "admin", "project"]'),
    ('["hi", "admin"], ["hI", "hi", "hi"]'),
    ('["4"], ["1", "2", "3", "4", "5"]'),
]

for case in test_list:
    assert total_match(*case) == case[1]
```