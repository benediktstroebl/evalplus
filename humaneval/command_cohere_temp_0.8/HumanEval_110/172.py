```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    if even_found:
        return "YES"
    else:
        return "NO"
```

The `exchange()` function takes two lists, `lst1` and `lst2`, as input and determines whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if any element in `lst1` is even. If any even element is found, it returns "YES," indicating that an exchange can be performed to make all elements in `lst1` even. Otherwise, it returns "NO," as no exchange can convert all elements in `lst1` to even numbers. 

This approach uses a concise and efficient any() with a map() combination to check if any even numbers are present in `lst1`, avoiding the need for explicit loops. Thus, it achieves the problem's goal while maintaining a clear and readable one-liner.