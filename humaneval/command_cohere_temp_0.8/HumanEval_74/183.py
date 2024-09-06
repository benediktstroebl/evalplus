```python
def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(val) for val in lst1)
    total2 = sum(len(val) for val in lst2)
    
    # If the total character count of lst2 is less than lst1, return lst2
    if total1 > total2:
        return lst2
    # If the total character count of lst1 is less than lst2, return lst1
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the first list lst1
    else:
        return lst1
```

This function utilizes Python's `sum` function in a clever way to calculate the total character count in each list. It then compares the counts and returns the list with the lower total character count, or the first list if the counts are the same. This approach eliminates the need for explicit loops, making the code more concise and efficient. 

This implementation avoids the need for explicit loops, making the code more concise and efficient while still achieving the desired result. No matter how many elements are in the list, this function will return the list with fewer characters.  This method also has a bonus of being efficient.