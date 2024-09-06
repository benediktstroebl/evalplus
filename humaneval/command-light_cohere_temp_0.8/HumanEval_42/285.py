```python
def incr_list(lst):
    lst.add(1)
    lst.add(2)
    lst
    lst.add(3)
    lst
    lst.add(4)
    lst
    lst
    lst.add(5)
    lst
    lst
    lst.add(5)
    lst
    lst
    lst.add(6)
    lst
    lst
    lst.add(7)
    lst
    lst
    lst.add(8)
    lst
    lst
    lst.add(9)
    lst
    lst
    lst.add(10)
    lst
    lst
    lst.add(11)
    lst
    lst

def test_incr_list(test_case):
    test_case.inc_list([1, 2, 3])
    assert lst == [2, 3, 4]
    test_case.inc_list([5, 3, 5, 2, 3, 3, 3, 9, 0, 123])
    assert lst == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    test_case.inc_list([6, 4, 6, 8, 7, 9, 10, 11, 12])
    assert lst == [7, 9, 10, 11, 12]
    test_case.inc_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert lst == [8, 9]
    test_case.inc_list([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    assert lst == [19]
```