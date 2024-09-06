```python
def median(l):
    # Sort the list in ascending order
    l.sort(l)
    
    # Calculate the median
    middle = len(l) // 2
    left_num = l[middle - 1]
    right_num = l[middle]
    if left_num > right_num:
        return (left_num + right_num) / 2
    else:
        return left_num

# Test the function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([21, 22, 21]) == 21.0
    assert median([1, 2, 3]) == 2.0
    assert median([1, 2, 3, 4]) == 3.0

# Driver code
test_median()
```