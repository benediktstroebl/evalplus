```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function uses a list comprehension to filter out even integers that are positioned at odd indices in the input list `lst`, and subsequently add them to the `even_odd` list. The result is the list containing the added even integers. 

This solution adheres to the problem statement, and the function can standalone, as it doesn't rely on any external variables or data that could impede its portability. 

If you would like to test this function, you can call it with a list of integers and examine the returned result, as seen in the example below: 
 ```python
print(add([4, 2, 6, 7]))
# Output: [2]
``` 
This will print `[2]` as this particular list's only odd index is the integer 2.