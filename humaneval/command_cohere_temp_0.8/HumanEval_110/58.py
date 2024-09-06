```python
def exchange(lst1, lst2):
    odd = lst1.pop()
    even = lst2.pop(0)
    if not lst1 or not lst2:
        return "NO"
    while lst1 and lst2:
        if lst1 and lst2:
            tmp = lst1.pop()
            lst2.append(tmp)
            tmp = lst2.pop(0)
            lst1.append(tmp)
        else:
            break
    if all(isinstance(n, int) and n % 2 == 0 for n in lst1):
        return "YES"
    return "NO"
```

The function `exchange()` works by exchanging odd and even numbers between the two lists to try and get all numbers in `lst1` to be even. The function continues this process of exchanging odd and even numbers until one of the lists is empty, at which point the other list will have at least one even number. The function then checks if all the numbers in `lst1` are even and returns the appropriate response. If the lists are emptied or contain non-integer values, the function returns "NO".