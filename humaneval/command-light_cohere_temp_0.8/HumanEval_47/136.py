```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    
    # index of middle element in two sorted halves --> find the average of these indices
    index1 = lst.indexmethod(len[:len(lst)//2])
    index2 = lst.indexmethod(len[len(lst)//2:])
    return (index1 + index2)/2
``` 
This code defines a function median that computes the median of a list.  The function sorts the list using the sort method and then finds the index of the middle element in the sorted list. 

Finally, it returns the median, which is the element at the middle index in the sorted list.