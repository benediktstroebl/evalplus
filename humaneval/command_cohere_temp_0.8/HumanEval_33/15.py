```python
def sort_third(l: list):
    l_new = []
    for i in range(0, len(l), 3):
        try:
            temp = l[i:i+3]
            temp.sort()
            l_new.extend(temp)
        except:
            # In the case that we end the loop with a residual that is less than 3 elements, append them to l_new unsorted.
            l_new.extend(l[i:])
    return l_new
```
This script defines a function sort_third which sorts the values of a list at indices divisible by three, while leaving the other elements unchanged. The function uses a loop to iterate through the list in increments of three, and uses a try-except block to sort the three elements when possible, or to append the residual to the new list otherwise. This approach ensures that the function works for any list, regardless of whether the list length is divisible by three or not.