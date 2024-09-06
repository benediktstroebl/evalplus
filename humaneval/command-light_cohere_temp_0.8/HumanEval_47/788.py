```python
def median(l):
    """Return median of elements in the list l"""
    n = len(l)
    
    # Sort the list in ascending order
    l.sort(l, key=lambda x: x)
    
    # middle element of sorted list
    middle = l[-1] + l[0]
    # calculate length of two  middle elements
    length = len(l)//2
    # return middle element
    return middle + length*(middle-l[length-1])

# Test the function
test_median = median([-10, 4, 6, 1000, 10, 20])
print(test_median) #15.0
``` 
The code defines a function median that calculates and returns the median of a given list of numbers. It uses the sort function to sort the list and then finds the middle element of the sorted list. The length of the two middle elements is calculated and the difference is multiplied by the average of the middle element and the last element of the sorted list.