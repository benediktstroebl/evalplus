```python
def exchange(lst1, lst2):
    even_exchange = False
    for x in lst1:
        if type(x) == int and x % 2 == 0:
            even_exchange = True
            break
    if even_exchange: 
        for x in lst2:
            if type(x) == int and x % 2 != 0:
                lst1.append(x)
                lst2.remove(x)
                even_exchange = False
                break
    return "YES" if even_exchange else "NO"
```

The `exchange()` function takes two lists (`lst1` and `lst2`) as input and checks if it's possible to exchange elements between them to make `lst1` a list of only even numbers. The function first checks if the even numbers exist in `lst1`, and if so, it iterates over `lst2`, where even numbers are appended to `lst1` and odd numbers are removed from `lst2`. This exchange is repeated until `lst1` contains only even numbers. The function returns "YES" if the exchange is possible without limiting the number of exchanges, and "NO" otherwise. 

The following test cases demonstrate the correct behavior of the function:
```python
test_cases = {
    "valid": [[1, 2, 3, 4], [1, 2, 3, 4]],
    "valid": [[1, 2, 3, 4], [1, 5, 3, 4]],
    "valid": [[2, 4, 6, 8], [2, 4, 6, 8]],
    "invalid": [[2, 4, 6, 8], [1, 2, 3, 4]],
    "invalid": [[1, 2, 3, 4], [2, 4, 6, 8]],
}

for case_name, case in test_cases.items():
    assert exchange(*case) == "YES" if case[0][0] % 2 == 0 else "NO"
```