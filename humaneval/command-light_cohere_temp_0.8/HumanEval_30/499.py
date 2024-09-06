```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
test_positive = []
for num in [-1, 2, -4, 5, 6]:
    test_positive.append(get_positive([num]))

print("Positive numbers:")
print(test_positive)
```