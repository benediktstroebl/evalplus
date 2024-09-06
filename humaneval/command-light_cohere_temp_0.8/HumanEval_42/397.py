```python
def incr_list(lst):
    lst[:] = [1] + lst  # Shift lisst to start with 1
    return lst

# Test cases
test_incr_list = []
test_incr_list.push([
    1, 2, 3])
test_incr_list.push([5, 5, 3, 5, 2, 3, 3, 9, 0, 123])
test_incr_list.push([6, 6, 4, 6, 3, 4, 4, 4, 10, 1, 124])

# Function test
def test_incr_list():
    test_incr_list = incr_list(test_incr_list)
    print(test_incr_list)

# Run tests
test_incr_list()
 ```