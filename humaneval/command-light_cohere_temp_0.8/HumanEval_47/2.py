```python
def median(lst):
    """Return the median of the list lst."""
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    
    # Check if the length of the list is even
    if n % 2 == 0:
        mid = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        mid = sorted_lst[n // 2]
    
    return mid
# Example usage
# Test the function with a list of numbers
med_value = median([-10, 4, 6, 1000, 10, 20])
print("Median:", med_value)
``` 
This script defines a self-contained function called median, which takes a list as input and returns the median value of its elements. The function first sorts the value of the list using the sorted() function and stores it in the sorted_lst variable. Then, it checks if the length of the list is even. In this case, the function returns the median of the middle two elements of the sorted list, which is (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]). If the length of the list is odd, the function returns the median of the middle element of the sorted list.