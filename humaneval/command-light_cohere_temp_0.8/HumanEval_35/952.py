```python
def max_element(lst):
    if not_elements(lst):
        return 0
    if len(lst) == 1:
        return lst[0]
    m = max(lst)
    return m

def test_max_element():
    lst1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    got1 = max_element(lst1)
    print("Result of lst1:", got1)
    assert got1 == 123

    lst2 = [-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    got2 = max_element(lst2)
    print("Result of lst2:", got2)
    assert got2 == 123

    lst3 = [1, 2, 3, 4, 5, 6]
    got3 = max_element(lst3)
    print("Result of lst3:", got3)
    assert got3 == 5

    lst4 = [5, 3, -5, 2, -3]
    got4 = max_element(lst4)
    print("Result of lst4:", got4)
    assert got4 == 5

    lst5 = [1, 2, 3, ,4, 5, 6]
    got5 = max_element(lst5)
    print("Result of lst5:", got5)
    assert got5 == 5

    lst6 = [1, 2, 3, 4, 5, ,6]
    got6 = max_element(lst6)
    print("Result of lst6:", got6)
    assert got6 is None

    return True

if __name__ == "__main__":
    test_max_element()
```
This code defines a function `max_element(lst)` that calculates and returns the maximum element from the input list `lst`. The `test_max_element()` function tests this function with various input lists, and the results are printed and compared to the expected values using `assert`.