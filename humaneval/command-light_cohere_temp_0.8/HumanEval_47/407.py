```python
def median(lst):
    n = len(lst) // 2 + 1
    if n == 1:
        return lst[0]
    a = lst[:n]
    b = lst[n:]
    return (a + b) / 2

# Tests
for _ in range(13):
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
``` 
This code defines a function median that calculates the median of a list of elements. The function first checks if the list has an even number of elements, in which case it returns the first element of the list. It then splits the this list into two halves, and returns the average of the elements in the first half and the elements in the second half as the median.