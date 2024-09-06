```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] += 1
    return l

# Test
test_incr_list = []
test_incr_list.push([5, [1, 2, 3])
test_incr_list.push([5, [5, 3, 5, 2, 3, 3, 9, 0, 123])

# Function call
result = incr_list(test_incr_list)

# Check if result is correct
if len(result) != len(test_incr_list):
    raise ValueError("Length of result is not equal to the original list.")

# Check for individual elements
for i in range(len(test_incr_list)):
    if result[i] != test_incr_list[i] + 1:
        raise ValueError(f"Incorrect result: {result[i]}, {test_incr_list[i]} + 1")
```