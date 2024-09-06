```python
def exchange(lst1, lst2):
    even_seen = False
    for x in lst1:
        if x % 2 == 0:
            even_seen = True
        else:
            if even_seen:
                return "NO"
    return "YES"
```

The function examines the first list, `lst1`, and determines whether it contains any odd numbers. If no odd numbers are found, it returns "YES". If an odd number is found but has already seen an even number, it returns "NO". This method has a time complexity of O(n) where `n` is the length of `lst1` and utilizes the modulo operator for checking evenness. 

This solution should be comparable in performance to the existing submissions as it is also O(n). 

This problem can also be solved in O(n) time without iterating the list multiple times like the above solution. Here is a markdown code block that outlines that solution:
```python
def exchange(lst1, lst2):
    even_found, odd_found = False, False
    for x in lst1:
        if x % 2:
            if even_found:
                return "NO"
            odd_found = True
        else:
            even_found = True
    return "YES"
```

This solution checks for the presence of even and odd numbers in the list simultaneously, setting a boolean flag for each. This allows us to return the appropriate response immediately after detecting the first odd number in the list, without needing to iterate the list multiple times.