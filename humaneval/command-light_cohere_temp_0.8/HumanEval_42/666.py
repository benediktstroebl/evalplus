```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([])  # Empty list
    assert not incr_list([10, 20, 30])  # List too large

# Main function
def main():
    print("Testing incr_list...")
    test_incr_list()

if __name__ == "__main__":
    main()
```
The function `incr_list` in this solution creates a new list with the items from the original list incremented by 1. The test suite includes several assertions to check the correctness of the `incr_list` function. The main function provides an entry point for executing the test suite and the `incr_list` function.