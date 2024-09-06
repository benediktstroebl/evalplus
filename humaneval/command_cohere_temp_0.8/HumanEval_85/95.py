```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' that stores the even integers positioned at odd indices from the input list 'lst'. It runs through each element in the list using a loop, checking if the index is even and the element is also even. If so, it includes this even element in the 'even_odd' list and lastly returns this list. 

To test this function, make sure to include a list of integers with even elements at odd indices, such as [4, 2, 6, 7], and check if the function's output is correct.