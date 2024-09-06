```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n//2] + l[n//2 - 1]) / 2
    else:
        return l[n//2]

# Test cases
for i in range(10):
    print(median([-10, -i, -100]))
```
The function median calculates the median of the list l. The function first checks if the list has an even number of elements. Then, it uses the condition to determine whether the list has an odd or even number of elements. The median is the average of the two middle numbers, if the list has an odd number of elements. If the list has an even number of elements, the median is the middle number.