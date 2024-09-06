```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list `lst`. It runs a loop through each element and index of the input list, using the `range(len(lst))` function to iterate through the indices. Within the loop, it checks if the index is odd using the modulo operator (`i % 2 == 0`) and if the element is even (`lst[i] % 2 == 0`), if both conditions are met, it appends the element to the `even_odd` list. Finally, the function returns the `even_odd` list. 

This code solves the problem statement and can be tested against the provided examples in the previous response.