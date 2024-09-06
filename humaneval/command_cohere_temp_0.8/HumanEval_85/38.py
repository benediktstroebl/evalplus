```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even numbers present at odd indices of the input list. It traverses the list, checking if the index is odd and the element is even, then it appends the element to `even_odd`. Finally, the function returns the `even_odd` list, which has all the even numbers present at odd indices of the input list. 

The following example will result in an empty list since none of the numbers in the index are at odd positions:
```python
add([1, 2, 3, 4, 5, 6])
``` 

While this other example will return the number 2, which is the only even number in an odd position in the list:
```python
add([4, 2, 6, 7])
``` 

You can test this function with different input lists to see if it correctly returns the even elements at odd indices of the list.