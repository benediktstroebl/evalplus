```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test case 1
print("Test case 1:", end="')
print("List: ", end="")
get_positive([-1, 2, -4, 5, 6])
print()

# Test case 2
print("Test case 2:", end="")
print("List: ", end="")
get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, -10])
print()

# Test case 3 (Should print [0])
print("Test case 3:", end=")")
print("List: ", end="")
get_positive([0, 5, 3, 2, -3, 3, 9, 7])
```