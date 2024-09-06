```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

if __name__ == "__main__":
    test1()
    test2()
```

The code defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The test cases `test1` and `test2` verify the correctness of the `incr_list` function by asserting that it returns the expected output for the given input. 

When you run the script, it will execute the test cases and print the output, or fail if the output is incorrect.