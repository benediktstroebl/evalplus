```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with a variety of lists
# Returns a list of successfully evaluated tests
tests = [
    [get_positive([-1, 2, -4, 5, 6])], 
    [get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])],
    [get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1])],
    [get_positive([-2, -3, -5, -8, -1])])

# Run function and append successful tests to results list
results = []
for test in tests:
    results.append(test)

print("Results: ", results)
```