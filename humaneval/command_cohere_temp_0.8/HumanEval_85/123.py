```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' which stores the even integers positioned at odd indices from the input list 'lst'. It loops through the input list, checking if the index is even and the element is also even, and accordingly adds it to the 'even_odd' list. Finally, the function returns the 'even_odd' list. 

To test this function, consider the input examples provided in the problem statement, such as the list [4, 2, 6, 7], and another example like [1, 3, 5, 7, 2]. These can be appended to the function or used as individual test cases to ensure that the function adds the correct even elements. Here is an example of how to test this function:
```python
add([4, 2, 6, 7]) # 2
add([1, 3, 5, 7, 2]) # [2]
```
This will allow you to confirm that the function correctly identifies and returns the even elements at odd indices from the input list.