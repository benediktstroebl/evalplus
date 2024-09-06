```python
def count_distinct_characters(string):
    return len(set(string.lower()))

x = "XYZ"
y = "jerry"

print(count_distinct_characters(x))  # This will print 3
print(count_distinct_characters(y))  # This will print 4
```