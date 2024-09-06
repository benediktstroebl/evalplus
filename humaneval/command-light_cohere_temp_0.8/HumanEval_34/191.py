Here's a self-contained Python script that defines a function unique that sorts and returns unique elements from a given list:
```python
def unique(l: list):
    seen = set()
    result = []
    for x in l:
        if x not in seen:
            seen.add(x)
            result.append(x
 more [ x]
    return result

# Test cases
test_unique_001 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_unique_002 = [2, 3, 4, 5, 6, 7]
test_unique_003 = [3, 2, 3, 8, 7, 9]
test_unique_004 = [0, 2, 3, 5, 4, 5]
test_unique_005 = [4, 5, 6, 7, 3, 2, 0]

# Test results
print(test_unique_001)
print(test_unique_002)
print(test_unique_003)
print(test_unique_004)
print(test_unique_005)
```

Please feel free to use this code and modify it according to your needs!