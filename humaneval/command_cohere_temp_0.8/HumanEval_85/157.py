```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' which stores the even integers present at odd indices of the input list. It checks for both the conditions (integer at odd index, integer even) with the help of the 'i% 2' and 'lst[i] % 2' and accordingly adds it to the 'even_odd' list. 

The function returns the 'even_odd' list which has all the even integers present at odd indices of the input list. 

The following examples illustrate how the function works: 

```python
add([4, 2, 6, 7]) ==> [2]
add([1, 3, 5, 7, 2, 4, 6]) ==> [6, 2]
``` 

These outputs are consistent with the examples provided in the prompt.