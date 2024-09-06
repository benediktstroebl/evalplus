```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test suite
tests = {
    "tests"
    "test_get_positive"
    {
        "def test_get_positive():
            assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
        }
    }
}

# Run the test suite
tests()
```