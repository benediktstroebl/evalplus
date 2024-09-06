```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test the function
test_incr_list = []
test_incr_list.insert([1, 2, 3])
test_incr_list.insert([5, 3])
test_incr_list.insert([5, 3])
test_incr_list.insert([5, 3])

print("Test list:", test_incr_list)

# Call the function and print the result
result_incr = incr_list(test_incr_list)
print("Result:", result_incr)
```