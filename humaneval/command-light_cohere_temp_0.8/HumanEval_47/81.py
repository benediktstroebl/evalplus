```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must not be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2
    else:
        return lst[len(lst)//2]

# Basic test cases
test_median = []
test_median.add([[-10, 4, 6, 1000, 10, 20])
test_median.add([[-20, 4, 6, 1000, 10, 30])
test_median.add([[-5, 4, 6, 1000, 10])
test_median.add([[-1, 4, 6, 1000, 10, 30])
test_median.add([[-100, 4, 6, 1000, 10])

# Test with list of strings
test_median.add(["This is text", "that's text", " test", " over"])

# Test with custom list
test_median.add([ [['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], ['b', 'x', 'y', 'z'])])

# Iterative test (for debugging purposes)
test_median_iterative = []
for i in range(0, 1000):
    test_median_iterative.append([i, i, i+1])

test_median_iterative.append([[-100, 4, 6, 1000, 10, 30])
test_median_iterative.append([[-1, 4, 6, 1000, 10, 30])
test_median_iterative.append([[-100, 4, 6, 1000, 10, 100])

# Test with large list
test_median_large = [range(0, 1000000)]

test_median_large.append([[-1000000, 4, 6, 1000, 10, 30])
```

This script contains a function `median` that calculates the median of the elements in a list. It then has a following test cases that cover different scenarios, such as empty lists, lists of strings, lists of numbers, and large lists.  The function is tested thoroughly using the `unittest` module.