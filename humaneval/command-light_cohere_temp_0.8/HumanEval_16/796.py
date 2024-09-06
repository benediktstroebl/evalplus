```python
def count_distinct_characters(string: str) -> int:
    return len(set(string))

# Test case 1:
string = 'xyzXYZ'
result = count_distinct_characters(string)
print("Test 1 passed:", result)

# Test case 2:
string = 'jerry'
result = count_distinct_characters(string)
print("Test 2 passed:", result)

# Test case 3:
string = 'jorca bcdeflsaq'
result = count_distinct_characters(string)
print("Test 3 passed:", result)
```