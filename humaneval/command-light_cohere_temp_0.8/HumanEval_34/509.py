```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x
   
    return result

# Test cases
tests = [
    [5, 3, 5, 2, 3, 3, 9, 0, 123],
    [2, 7, 91, 911],
    ['three'],
    [123, []]
]

for test in tests:
    actual = unique(test)
    print(f"Test: {test} -> {actual}")
    print()
```  This code defines a function unique that sorts and returns unique elements from the input list. 

Test cases are provided, and the function is evaluated against each test. The results are printed to the console.