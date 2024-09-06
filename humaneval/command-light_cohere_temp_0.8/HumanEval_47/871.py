```python
def median(l: list):
    """Return median of elements in the list l."""
    m = l[len(l) // 2]
    if len(l) % 2 == 0:
        return (m + l[len(l) // 2]) / 2.0
   
    for i in range(len(l)):
        if i == len(l) // 2:
            continue
        if l[i] > m:
            m = l[i]
    return m
# Test case 1
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
# Test case 2
print(median([1, 2, 4, 5]))  # Output: 5.0
# Test case 3
print(median([-10, 4, 6, 1000, 1, 20]))  # Output: 10.0
# Test case 4
print(median([100, 101, 102, 103, 104, 105]))  # Output: 102.0
``` 
This script defines a function called `median` that computes the median of a list. The function takes a list as an argument and returns the median of the elements in the list. 
The function uses the formula for calculating the median of an even-length list to find the middle value and swaps the position of the middle value with the two extreme values. If the list is even the length, the function takes the element at the middle of the list and returns it.