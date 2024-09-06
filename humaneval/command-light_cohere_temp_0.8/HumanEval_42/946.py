```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.extend(1)
    l.extend(2)
    l.extend(3)
    l.extend(4)
    l
    l = [x + 1 for x in l]
    return l

# Test cases
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 5, 2, 3, 3])
test_incr_list.append([9, 6, 4, 6, 3, 4, 4, 10, 1, 124])

# Function Call
result = incr_list(test_incr_list)

# Print Results
print("Test Cases:", end , sep="\n")
print("Results:", end , sep="\n")
for item in result:
    print(item, end=" ")
```