```python
def sort_third(lst):
    return lst[:] if all(i % 3 == 0 for i in lst) else lst

# Test cases
tests = [
    ( [1, 2, 3], ),
    ( [5, 6, 3, 4, 8, 9, 2],),
    ( [5, 6, 9, 3], ),
    ( [5, 6, 8, 9], [3, 4, 6, 7]),
    ( [1, 2, 3, 4, 5, 6], ),
    ( [8, 9, 2, 6, 3], [3, 6, 9, 4])
]

for case in tests:
    actual = sort_third(case[0])
    expected = case[1]
    print(f"Case {i}: actual({actual}) -> expected({expected})")
```  This code defines a function that takes a list and returns a list with lists that are divisible by 3 at the index that are not divisible by 3, and the other values are equal to the values at the corresponding index in the original list but sorted.