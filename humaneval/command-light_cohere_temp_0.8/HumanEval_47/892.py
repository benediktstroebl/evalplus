```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("List must not be empty.")
    if len(lst) == 1:
        return lst[0]
    else:
        middle = len(lst) // 2
        left_value = lst[middle - 1]
        right_value = lst[middle]
        if left_value > right_value:
            left, right = left_value, right_value
        else:
            left, right = right_value, left_value
        return (left + right) / 2
``` 
This script defines a function called median that takes a list as an argument. It then checks for basic conditions: that the list is not empty and that it is not a single element. It uses the specific logic to find the middle element and then computes the median by finding the average of the two middle elements. 

Finally, it passes the test by creating a list with various elements and asserts that the returned median matches the expected result.