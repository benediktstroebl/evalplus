```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test the function with a list of different elements
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result = incr_list(test_list)
if result == [6, 4, 6, 3, 4, 4, 10, 1, 124]:
    print("Function passed tests with list:", test_list)
else:
    print("Function failed tests with list:", test_list)
``` 
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. It uses a easy for a specific list and uses the same list to test the function.