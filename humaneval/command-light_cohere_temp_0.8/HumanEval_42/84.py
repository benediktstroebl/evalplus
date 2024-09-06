```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [i + 1 for i in l]
    return new_list

# Test the function with known good inputs/outputs
# Test case 1:
# [1, 2, 3] -> [2, 3, 4]
# Test case 2:
# [5, 3, 5] -> [6, 4, 6]
# Test case 3:
# [5, 3, 9] -> [6, 4, 6]
# Test case 4:
# [0, 123] -> [1, 124]
# Test case 5:
# [3, 3, 0] -> [4, 3, 10]
# Test case 6:
# [1, 2, 3, 2] -> [2, 3, 4]

def test_incr_list():
    for test_case in [test_case() for _ in range(10)]:
        assert incr_list(test_case) == test_case

test_incr_list()
```