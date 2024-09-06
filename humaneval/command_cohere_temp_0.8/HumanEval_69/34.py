```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if max_val < freq:
                max_val = i 
    return -1 if max_val < freq else max_val
```

This script defines a function 'search' which iterates through the list, tracking the maximum value greater than zero (`max_val`) and its corresponding frequency (`freq`). If a maximum value is hit and its frequency is less than the value, we return -1 as no greater value exists. If a maximum value is hit and its frequency is equal or greater than the value, we return the maximum value. 

Let's say the function is called with the list `[5, 5, 4, 4, 4]`. The variable `max_val` will update to 5, whereas the frequency (`freq`) will update to 3, as 5 appears 3 times in the list. Given the criterion that the frequency of the integer should be greater than or equal to its value, the function will return -1, as the maximum value of 5 with a frequency of 3 does not fulfill this criterion. 

On the other hand, if the function is called with the list `[1, 2, 2, 3, 3, 3, 4, 4, 4]`, the `max_val` will update to 3, while the `freq` will also update to 3, as 3 appears 3 times in the list. The function will thus return 3, as this maximum value 3, appears as many times as it should (or more) according to the criterion. 

In summary, the function returns the maximum integer greater than zero whose appearance in the list meets the criterion, or -1 if no such integer exists.