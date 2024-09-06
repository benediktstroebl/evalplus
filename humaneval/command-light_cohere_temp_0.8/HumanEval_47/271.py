```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

#Test case 1
assert median([3, 1, 2, 4, 5]) == 3

#Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15

#Test case 3
assert median([2, 4, 5, 6]) == 5

#Test case 4
assert median([1, 2, 3, 4, 5]) == 2

#Test case 5
assert median([-1, -2, -3, -4, -5, -6)) == -3

```
This Python code defines a function median that calculates the median of a list. It then tests the tested using a wide variety of input lists. The test cases aim to cover various scenarios and ensure that the function works correctly for different lists of elements.