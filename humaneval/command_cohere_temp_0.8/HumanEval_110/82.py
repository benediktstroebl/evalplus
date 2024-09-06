```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    return "YES" if even_found and all(map(lambda x: x in lst2, lst1)) else "NO"
```
The code defines a function `exchange` taking two lists `lst1` and `lst2` as inputs. The problem is to determine whether it's possible to exchange elements between the two lists to make `lst1` contain only even numbers. The function uses `any` and `all` with a lambda function to determine if there are any even numbers in `lst1` (indicating an even number can be exchanged) and if all elements in `lst1` are in `lst2` (indicating all elements can be exchanged). Returning "YES" if both conditions are met and "NO" otherwise.  This solution assumes the lists contain unique values.