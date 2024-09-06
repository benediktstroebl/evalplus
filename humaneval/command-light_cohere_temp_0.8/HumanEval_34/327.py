```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Test case 1: Test function with list of numbers
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = unique(test_case1)
assert result == [0, 2, 3, 5, 9, 123]

# Test case 2: Test function with list of strings
test_case2 = ["apple", "orange", "banana", "grapefruit", "strawberry"]
result = unique(test_case2)
assert result == ["apple", "orange", "banana", "grapefruit"]
```  This code defines a function `unique` that returns a sorted list of unique elements from the input list. The code also includes two test cases to verify the correctness of the `unique` function.