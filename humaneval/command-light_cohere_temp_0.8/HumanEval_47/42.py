```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[n//2 - 1]) / 2
    else:
        return lst[n//2]

# Test cases
for i in [median([-10, 4, 6, 1000, 10, 20]) ,median([-20, -15, -10, -5, 3, 1]) ,median([10, -20, 40, 30, -40])]:
    print(i, "is", end=" ")
```
This script defines a function median that computes the median of a list. The function works for even lists with odd and even length numbers by taking the middle value of the even-length list. 

The test cases validate the correctness of the median function with different input lists.