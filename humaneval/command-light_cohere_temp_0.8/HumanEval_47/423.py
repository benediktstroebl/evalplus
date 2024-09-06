```python
def median(l):
    # Sort the list in ascending order
    l.sort(l)
    
    # Calculate the median
    middle = l[len(l)//2]
    left = 0
    right = len(l) - 1
    
    while left < right:
        if l[left] == middle:
            left += 1
        elif l[right] == middle:
            right -= 1
        else:
            l[left], l[right] = l[right], l[left]
            middle = l[left]    
            
    return middle

# Test case
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This Python code defines a function called `median` that computes the median value of a list of numbers. It sorts the list and then calculates the median by selecting the middle value of the sorted list. The code also provides test cases to ensure that the function works as expected and returns the correct median value.