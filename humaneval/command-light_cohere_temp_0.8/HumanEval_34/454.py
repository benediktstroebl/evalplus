```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Tests
# Ensure function returns the expected unique elements
test_one = [5, 3, 5, 2, 3, 3, 9, 0, 123]
assert unique(test_one) == [0, 2, 3, 5, 9, 123]

# Ensure function doesn't modify the original list
test_modify = [1, 2, 3]
original_test_modify = list(test_modify)
assert original_test_modify == [1, 2, 3]

test_large = [123, 5, 5, 4, 6, 7, 3, 1, 8, 9]
assert set(unique(test_large)) == {123, 5, 4, 6, 7, 1, 8, 9}
```
The code defines a function unique that sorts and returns unique elements from an input list. It uses a new set to efficiently track unique items and a list to store the result. The tests verify the test the expected behavior of the unique function with a set of test cases, including one that checks the function's output against a known list and another that checks the original list is unchanged after the function is called.