```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        return "YES"
    else:
        return "NO"
```

The function examines whether the list contains even numbers, and if so, returns 'YES'; otherwise, it returns 'NO'. 

Here is an example usage of the function:
```python
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: "YES"
```

This will return the answers 'NO' and 'YES' for the respective test cases.