```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique)
    return result

# Tests
test_pass = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test Pass:", test_pass)

test_fail = unique([1, 2, 3])
print("Test Fail:", test_fail)
```
This Python code defines a function called unique that takes a list lst as input and aims to return a new list with unique elements from the original. It uses a unique set of elements and initializes a new list result. Then, it loops through the elements of the input list and adds them to the unique set if they are not already present. Finally, the new list result is returned, containing only the unique elements from the input list. The code also includes two test cases: one pass and one fail, which are intended to verify the functionality of the unique function.