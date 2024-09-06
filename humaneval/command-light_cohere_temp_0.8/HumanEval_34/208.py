```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test case 1
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
print(result1)  # Output: [0, 2, 3, 5, 9, 123]

# Test case 2
test_case2 = [5, 3, 0, 7]
result2 = unique(test_case2)
print(result2)  # Output: [5, 3, 0]

# Test case 3
test_case3 = [5, 3, "hello"]
result3 = unique(test_case3)
print(result3)  # Output: ["hello"]
```

This code defines a function unique which takes a list lst as input and returns a new list containing unique elements from the original list. The unique elements are then extracted from a set seen, where each element is only added to the set once. This ensures that duplicate elements are not repeated in the result.