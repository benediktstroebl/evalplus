```python
def is_sorted(lst):
    dups = {}
    for x in lst:
        if x in dups:
            dups[x] += 1
        else:
            dups[x] = 1
    
    for x in dups:
        if dups[x] > 1:
            return False
    
    return all(x <= y for x, y in zip(lst, lst[1:]))
```

The function implements the problem statement's logic by first checking for duplicates and then checking if the list is sorted assuming no duplicates. To check for duplicates, the function uses a dictionary to store the frequency of each number in the list. If more than one instance of a number is found, the function returns false since the criterion states that lists with more than one duplicate are not considered sorted. 

After processing the duplicate check, the function then uses a list comprehension to check if each element is greater than or equal to the subsequent element. If this holds for all elements, then the list is sorted and the function returns true. If either of these conditions is not met, the function returns false. 

Overall, the code compactly solves the problem using basic Python data structures and logic. 

The function above is self-contained and does not require any external libraries or modules. It should be noted that the function assumes that the list passed in is comprised of only integers. It is also worth mentioning that the function is not optimized for large lists as it requires iterating over the list multiple times.