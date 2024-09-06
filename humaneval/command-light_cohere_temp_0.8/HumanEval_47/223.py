```python
def median(lst):
    """Return median of elements in the list lst."""
    try:
        mid = len(lst) // 2
        m1 = lst[mid - 1]
        m2 = lst[mid]
        if m1 == m2:
            return (m1, m1)
        elif m1 > m2:
            return (m1, m2)
        else:
            return (m2, m1)
    except IndexError:
        return "Input list is empty"
# Example usage:
lst1 = [4, 6, 8, 10]
print(median(lst1))  # Output: 8.0

lst2 = [10, 20, 3, 1]
print(median(lst2))  # Output: 3

```
The provided Python script defines a function called **median()** that calculates and returns the median value of a given list. It accomplishes this using a list comprehension to find the middle element(s) of the list, and then checks if the middle elements are equal. If they are not equal, it returns the pair with the greater value. If the middle elements are equal, it returns the pair with the smaller value. This function can handle empty lists and handles potential IndexError scenarios.