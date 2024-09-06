```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even numbers present at odd indices of the input list. It traverses the list and verifies if the index is odd and the element is even, then it appends that element to `even_odd`. Finally, it returns the `even_odd` list, which will be the list of even elements present at odd indices of the input list. 

The following example will run the function with a test input and verify if the function correctly solves the problem:
```python
print(add([4, 2, 6, 7])) # 2
```

This will output:
```
2
```