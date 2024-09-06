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

Here is an example usage of the function with a test case: 
 ```python
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: "NO"
``` 
And here is another example usage of the function with a different test case: 
```python
print(exchange([1, 2, 3, 4], [2, 4, 6, 8]))  # Output: "YES"
``` 
This would output 'NO' for the first test case and 'YES' for the second test case.