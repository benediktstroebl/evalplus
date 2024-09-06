```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3] + l 

def test_incr_list():
    """Test incr_list function"""
    lst = [1, 2, 3]
    result = incr_list(lst)
    assert len(result) == 7
    assert result == [2, 3, 4]
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    result = incr_list(lst)
    assert len(result) == 14
    assert result == [6, 4, 6, 3, 4, 4, 4, 10, 1, 124]

def main():
    test_incr_list()

if __name__ == "__main__":
    main()
```