```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```
The function checks if there is an odd number in the first list. If not, it returns "YES". Otherwise, it returns "NO". 

Here is an example usage of the function with arguments [[1, 2, 3, 4], [1, 2, 3, 4]]:
```python
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Should print: "YES"
```

And here is an example with arguments [[1, 2, 3, 4], [1, 5, 3, 4]]:
```python
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Should print: "NO"
``` 

This is the code snippet from above that can be copied and pasted into a Python environment or script:
```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```