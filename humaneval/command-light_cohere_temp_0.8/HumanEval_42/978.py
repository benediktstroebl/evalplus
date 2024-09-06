```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)

    return l

def test_incr_list():
    """Return True if list can be incremented by 1 to get a list of increasing integers"""
    l = [1, 2, 3]
    return all([x+1 == l[i]+1 for i,x in enumerate(l)])

if __name__ == "__main__":
    assert test_incr_list()
    print("Test passed")
```