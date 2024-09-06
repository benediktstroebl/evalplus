```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    n = len(l)
    result = [i+1 for i in l]
    return result

def test_incr_list():
    """Unit tests for incr_list function"""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert lst == incr_list(lst) == expected
    return True

def main():
    if __name__ == "__main__":
        print("Running unit tests..." + "\n")
        test_incr_list()
        print("Tests finished successfully..." + "\n")

if __name__ == "__main__":
    main()
```
This script defines a function `incr_list` that returns a list with elements incremented by 1, and a test function `test_incr_list` with unit tests for the `incr_list` function.  It expected output is when you run this script will be the success message for the tests.