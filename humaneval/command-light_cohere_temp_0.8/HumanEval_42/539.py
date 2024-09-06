```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [1]

def test_incr_list():
    """Test the incr_list function"""
    l = [1, 2, 3]
    assert l == incr_list(l)
    assert [2, 3, 4] == incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    assert l[-1] == 1
    assert l[-2] == 2

# Main function
def main():
    test_incr_list()

if __name__ == "__main__":
    main()
```
The test_incr_list function performs the following tests:
1. test_incr_list: Test the behavior of the incr_list function with a list and assert statement to verify the output.
2. test_incr_list: Test the behavior of the incr_list function with a list and assert statement to verify the output of the list with the expected elements.
3. test_incr_list: Test the behavior of the incr_list function with a list and assert statement to verify the output of the list with the expected elements and the last element.