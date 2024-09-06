```python
def median(lst):
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    mid = len(lst) // 2 + 1
    if lst[mid - 1] > lst[mid]:
        mid = mid - 1
    return (len(lst) % 2 == 0 and lst[mid] or (lst[mid - 1] + lst[mid]) / 2)
# Example usage
lst = [5, 10, -10, 3, 12, 8, 7]
result = median(lst)
print("Median:", result)
``` 
This code defines a function median that computes the median of a list. It uses a tested to ensure that the list is not empty, and if it is, it returns the median value of the list. If the list is empty or ValueError is raised.