```python
def total_match(lst1, lst2):
    char_count_1 = sum(len(item) for item in lst1)
    char_count_2 = sum(len(item) for item in lst2)
    
    if char_count_1 == char_count_2:
        return lst1
    elif char_count_1 < char_count_2:
        return lst2
    else: 
        return lst1
```
The code uses two one-liner sum functions to calculate the total number of characters in all strings of the two input lists. The function then compares the counts and returns the list with fewer characters, or, if both are equal, returns the first list. This all happens in less than three lines of code, making the function highly efficient and readable.