```python
def exchange(lst1, lst2):
    even_found = any(x % 2 == 0 for x in lst1)
    if even_found:
        return "YES"
    else:
        return "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as input and returns a string indicating whether it is possible to exchange elements between them to make `lst1` a list of only even numbers. The function checks if any element in `lst1` is even. If true, it returns "YES" because we can remove all odd numbers from 'lst1' by exchanging them with the matching numbers in `lst2`. If no element in `lst1` is even, it returns "NO" because no exchange can make all elements in `lst1` even. 

Here is a simple test case to verify the code:
```python
test_case = [[1, 2, 3, 4], [1, 2, 3, 4]]
answer = exchange(test_case[0], test_case[1])
assert answer == "YES"
```

The expected output is "YES" because the function can exchange the elements between the two lists to make the first list contain only even numbers.  This verifies that the code is functioning as expected.