```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. characters()})

# Testing the function
x = 'xyzXYZ'
result = count_distinct_characters(x)
print(result)
# Should print 3

y = 'Jerry'
result = count_distinct_characters(y)
print(result)
# Should print 4
```