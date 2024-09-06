```python
def median(l):
    # Sort the list
    l.sort(l)
    
    # Take the median
    middle = len(l) // 2
    left = 0
    right = middle - 1
    if l[middle] > l[right]:
        temp = l[middle]
        l[middle] = l[right]
        l[right] = temp
        middle = right
    elif l[middle] < l[right]:
        temp = l[right]
        l[right] = l[middle]
        l[middle] = temp
        middle = right
    else:
        pass
    
    if l[middle] == 0:
        return 0
    else:
        return l[middle]

# Unit tests
test_median = []
test_median.add([range(0, 11))
test_median.add([range(1, 21))
test_median.add([range(2, 22))
test_median.add([range(3, 23))

for item in test_median:
    print(median(item))
 ```