```python
def incr_list(lst):
    lst[0] = 1
    return lst

# Test case 1
def test_incr_list1():
    test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert incr_list(test_list) == expected

# Test case 2
def test_incr_list2():
    test_list = [1, 2, 3]
    expected = [2, 3, 4]
    assert incr_list(test_list) == expected

if __name__ == "__main__":
    test_incr_list1()
    test_incr_list2()
```
This script defines a function incr_list that increments the first element of an input list by 1 and returns the modified list. Two test cases are test_incr_list1 and test_incr_list2 are defined to verify the correctness of the incr_list function by applying it to test lists and comparing the returned lists with expected results.