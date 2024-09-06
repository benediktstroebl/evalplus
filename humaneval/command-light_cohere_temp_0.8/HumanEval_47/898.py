```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
```

The provided solution calculates the median of a list using the following steps:
1. Calculate the length of the list. Then, check if the list is even even length, indicating an even number of elements. If the list has an length that is odd, the median is simply the middle element.
2. Calculate the median using element in the middle of the list, if the list has an even number of elements. If the list has an length that is odd, the median is calculated by taking the average of the two middle elements.