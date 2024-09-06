```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return lst[0]
    m = n//2
    if n % 2 == 0:
        return (lst[m-1]+lst[m])/2
    return lst[m]

# Test 1: This list has an even length
[-10, 4, 6,10,20]
median([-10, 4, 6, 10, 20]) == (10+20)/2 = 15

# Test 2: One element in the list
[-10]
median([-10]) == -10

# Test 3: Two equal elements
[-10,-10]
median([-10, -10]) == 0

# Test 4: Three elements in the list
[-10, -5, -3]
median([-10, -5, -3]) == -5

# Test 5: Large list
median([-10, -20, -30, -40]) == -40
```
The function median() calculates the median of a list of elements. It handles special cases: when the list has an even length, it returns the average of the middle two elements; otherwise, it returns the middle element. The function also handles the simple cases with one or two elements.