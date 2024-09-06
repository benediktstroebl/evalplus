```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Basic tests
print("Basic Tests Passed:", end="")
for _ in range(5):
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])))

# Edge case tests
print("\nEdge case tests Passed:", end="")
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, None]))

# Type tests
print("\nType tests Passed:", end="")
x = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
y = max_element(x)
print(type(y), y)
```