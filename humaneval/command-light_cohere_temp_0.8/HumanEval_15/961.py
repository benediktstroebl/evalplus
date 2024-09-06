```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 up to n.
    >>> s1 = string_sequence(0)
    '0'
    assert s1 == '0'
    
    >>> s2 = string_sequence(5)
    '0 1 2 3 4 5'
    assert s2 == '0 1 2 3 4 5'
    
    >>> s3 = string_sequence(7)
    '0 1 2 3 4 5 6 7'
    assert s3 == '0 1 2 3 4 5 6 7'
    
    >>> test_fail = string_sequence(-1)
    assert_equal(test_fail, "")
    def assert_equal(test1, test2):
        assert test1 == test2, "Both inputs are not equal"
```