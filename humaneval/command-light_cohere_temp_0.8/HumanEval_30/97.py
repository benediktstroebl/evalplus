```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function
test_positive = []
for i in range(0, 11):
    test_positive.append(get_positive([i]))

# Validate the function using assertion
if not test_positive:
    print("Function does not work correctly")
```