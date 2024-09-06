```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(l[-1] + 1)
    return l

# Test function to check incr_list function
def test_incr_list():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    actual = incr_list(test_list)
    assert list(set(expected)) == set(actual)

# Main function to call test_incr_list function
def main():
    test_incr_list()

if __name__ == "__main__":
    main()
``` 
This code defines the `incr_list` function, which adds one to the last element of the input list and returns the updated list. The `test_incr_list` function tests whether the `incr_list` function works correctly by comparing the expected and actual values of a list. Finally, the `main` function is used to call the `test_incr_list` function, which starts the execution of the test and the main function.