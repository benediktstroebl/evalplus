```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
median_([3, 1, 2, 4, 5]) # Should return 2.5
median([-10, 4, 6, 1000, 10, 20]) # Should return 15.0
median([5, 5, 5]) # Should return 5.0
``` 
The function median in the script calculates the median of the elements in the list lst. The function first checks if the list has an even number of elements. If the list has an odd number of elements, the median is the middle element. Otherwise, the median is the average of the two middle elements. 

This self-contained function can be used to solve the problem and pass tests easily.