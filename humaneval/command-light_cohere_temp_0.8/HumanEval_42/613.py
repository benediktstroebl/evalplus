```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    assert len(result) == n
    assert all(result[i] == i + 1 for i in range(n))
    return result

# Example usage
lst = [1, 2, 3]
result = incr_list(lst)
print(result)  # Output: [2, 3, 4]
```
The function incr_list takes a list l as input and returns a new list with elements from the input list incremented by 1. The function uses list comprehension with a generator expression to create the new list, and then performs some assertions to ensure the correctness of the output. The example usage demonstrates how to call the incr_list function with a list of integers and print the resulting list.