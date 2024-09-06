```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

#Test cases 

values_test = [1, 2, 3, 'abc', {}, [1, 2, 3])

print("Test case 1: " + values_test)
print("Expected Output: [1, 2, 3]")

values_test2 = [1, 2, 3, 'abc', [], ()]

print("Test case 2: " + values_test2)
print("Expected Output: []")

values_test3 = [1, 2, '30', 10.14]

print("Test case 3: " + values_test3)
print("Expected Output: [1, 2, 10. fedora of Python strings")
```