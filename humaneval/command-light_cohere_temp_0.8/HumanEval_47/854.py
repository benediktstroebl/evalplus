```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test suite for median function
def test_median():
    try:
        # Sample list with odd and even elements
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert median(list1) == 5.0
        assert median([-10, 4, 6, 1000, 10, 20]) == 10.0

        # Sample list with all even elements
        list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert median(list2) == 5.0

        # List with duplicates
        list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        assert median(list3) == 5.0

        # List with one element
        list4 = [10]
        assert median(list4) == 10.0

        # List with no elements
        list5 = []
        assert median(list5) == None
```