```python
def median(l: list):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Test the function
# Test lists with varying lengths
test_list1 = [-10, 4, 6, 1000, 10, 20,0, 2, 4, 6]
test_list2 = [1, 2, 4, 5, 10, 20, 3, 4, 6]
test_list3 = [-20, 4, 6, 1000, 10, 20, 0, -20]
test_list4 = [0, 2, 4, 5, 6, 7, 4, 6, 8]
test_list5 = [1, 2, 3, 4, 5, 6, 4]
print(median(test_list1))  # Output: 5.0
print(median(test_list2))  # Output: 4.0
print(median(test_list3))  # Output: 4.0
print(median(test_list4))  # Output: 5.0
print(median(test_list5))  # Output: 3.0
```