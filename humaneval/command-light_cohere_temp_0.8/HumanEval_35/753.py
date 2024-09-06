```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

#Test cases
test_max_element = [
    ("[-5, 3, 2, -3, 7]," -> 3),
    ("[123, 456, 789, 123]", " -> 456),
    ("[-122, -90, -35]", " -> -35"),
    ("[1, 2, 3, 4, 5]", " -> 5"),
    ("[0, 9, -8]", " -> -8"),
]

for test in test_max_element:
    got = max_element(test)
    assert got == test[1], "Test " + str(test) + " failed"
```