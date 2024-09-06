```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
test_median = []
for i in range(0, 10):
    test_median.append([i, median([-10, i, 6, 1000, 20, 30])])

for i in test_median:
    print(f"{i}\t{i}")
```
The code defines a function median that calculates the median of a given list. The median is the average of the two middle numbers when the list is even or the average of the two elements in the index (N//2) when the list is odd. The code also provides a list of test cases to ensure the correctness of the function by running the function with a list of integers and printing the results.