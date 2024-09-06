```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    sorted(lst)
    # The median is the middle element
    middle = len(lst) // 2
    if len(lst) % 2 == 1:
        return lst[middle]
    else:
        return (lst[middle-1] + lst[middle]) / 2

# Test the function with a list of numbers
test_lst = [10, 20, 40, 4, 6, 2, 3, 1]
median_test_lst()
print("Median:", end="fit")
``` 
This Python code defines a function `median` that calculates and returns the median of a given list of numbers. The function utilizes the sorting the list in ascending order and then determines the median based on whether the list has an even or odd number of elements.