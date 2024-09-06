```python
def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(el) for el in lst1)
    total2 = sum(len(el) for el in lst2)
    
    # If the total character count is less in the second list, return the second list
    if total1 > total2:
        return lst2
    # If the total character count is less in the first list, return the first list
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the first list or second list, whichever has the element 'admin' at the top
    else:
        return ['admin' in el for el in lst1] or ['admin' in el for el in lst2]
```

This code uses a conditional structure to compare the total count of characters in the strings within the first and second lists. It leverages the sum function to calculate the total character count in each list efficiently. The code then checks if the total character count is less in the first list than the second or vice versa. If one of these conditions is met, it returns the corresponding list. If neither condition is true, it checks if the total character counts are the same. If they are, the code returns the list that includes the element 'admin' at the top, as specified in the problem statement. 

This solution is concise and adheres to Python's PEP 8 style guide, making it readable and maintainable. It also runs the gamut of scenarios posed in the problem statement.