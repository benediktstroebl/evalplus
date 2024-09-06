```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [i for i in l if i % 3 != 0] + [i for i in l if i % 3  == 0]

# Test cases
tests = [
    "Input: [1, 2, 3]
    "Input: [5, 6, 3, 4, 8, 9, 2]"
    "Input: [5, 6, 8, 9, 3, 4, 2]"
]

# Function call and test results
for t in tests:
    assert sort_third(t) == [2, 6, 3, 4, 8, 9, 5], f"Failed for: {t}"
```