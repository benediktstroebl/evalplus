```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) < 1:
        raise ValueError("Input list must not be empty.")
    if len(lst) == 1:
        return lst[0]
    mid = len(lst) // 2
    if lst[mid] > lst[mid - 1]:
        mid = (mid - 1) + 1
    median = (lst[mid] + lst[mid - 1]) / 2
    return median

# Tests
def test_median():
    list1 = [-10, 4, 6, 1000, 10, 20]
    assert median(list1) == 15.0

def test_empty():
    list1 = []
    assert median(list1) is None

def test_single():
    list1 = [1]
    assert median(list1) == 1.0

def test_list():
    list1 = [10, 20, 30, 40, 50]
    assert median(list1) == 35.0

test_out = {
    'test_median():',
    'test_empty():',
    'test_single():'
}
test_out_list = [(type(subtest), subtest) for subtest in test_out]
for test in test_out_list:
    print(f"{test[0]}: {test[1]}")
 ```