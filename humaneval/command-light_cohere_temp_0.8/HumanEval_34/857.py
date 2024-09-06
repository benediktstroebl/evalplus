```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not)== [] and seen.

#Test case 1:
test_unique = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_unique)

#Test case 2:
test_unique2 = unique([5, 5, 2, 3])
print(test_unique2)

#Test case 3:
test_unique3 = unique([1, 2, 3, 4, 5, 6])
print(test_unique3)
```