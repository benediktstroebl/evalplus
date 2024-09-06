```python
def unique(lst):
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result

# Example usage:
# Test 1: Valid list
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print("Test 1 result: ", result)

# Test 2: Empty list
result2 = unique([])
print("Test 2 result:", result2)

# Test 3: Duplicate values
result3 = unique([5, 5, 0])
print("Test 3 result:", result3)
```
This script defines a function called unique that takes a list lst as input and returns a list of unique elements from the input. It uses a set to keep track of seen elements and then iterates through the input list, appending unique elements to the result list. The function also includes example usage to test the function with various input lists.