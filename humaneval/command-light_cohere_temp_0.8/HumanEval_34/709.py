```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

#Test cases
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))  # Output: [0, 2, 3, 5, 9, 123]
test_string = "unique([5, 3, 5, 2, 3, 3, 9, 0, 123])"
print(eval(test_string))  # Output: [0, 2, 3, 5, 9, 123]

# Custom test framework (your code here)
def custom_test():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```