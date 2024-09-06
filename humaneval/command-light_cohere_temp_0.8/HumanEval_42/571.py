```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test suite for the incr_list function
def test_incr():
    try:
        l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
        result = incr_list(l)
        assert l == result, "Incorrect result"
        assert len(result) == 10, "Incorrect length"
        assert all(result[i] == i + 1 for i in range(1, 10)), "Incorrect increment"
    except AssertionError as e:
        print(e)
    return_pass

# Main function
def main():
    test_incr()

if __name__ == "__main__":
    main()
```