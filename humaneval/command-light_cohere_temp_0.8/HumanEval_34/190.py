```python
def unique(l: list):
    return sorted(set(l))

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([7, 7]) == [7]
assert unique([a for a in range(10)]) == list(range(10))

```  This script defines a function unique that returns a sorted set of unique elements in the input list. It also provides several test cases to validate the correctness of the unique function.