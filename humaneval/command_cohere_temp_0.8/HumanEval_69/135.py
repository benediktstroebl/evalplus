```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val:
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function `search` takes a list of integers as input and returns the greatest integer that meets the conditions stated in the problem. It first finds the maximum value in the list and the frequency of each integer in the list. Then it iterates through each integer in the list, comparing its value with the frequency of appearances. If it finds an integer greater than the current maximum value and the frequency of appearances is greater than or equal to the integer itself, it updates the maximum value and frequency. After the loop, if the maximum value is equal to its frequency and is zero, meaning there are no other integers greater than and with a frequency equal to themselves, it returns -1. Otherwise, it returns the maximum value. 

The code works under the assumption that the list contains only positive integers. It would be necessary to add a check for the validity of the input if the list could contain invalid data.