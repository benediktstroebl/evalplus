```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_even_in_lst2 = any(map(lambda x: x % 2 == 0, lst2))
    if even_found and count_even_in_lst2:
        return "YES"
    return "NO"
```

The function **exchange** takes in two lists, `lst1` and `lst2`, and returns "YES" if it's possible to exchange elements between them so that `lst1` contains only even numbers. This function checks if there is at least one even number in both `lst1` and `lst2`. If both conditions are satisfied, it returns "YES," and if neither condition is true, it returns "NO." 

Here is a simple test case to demonstrate this function:
```python
test_case = [[1, 2, 3, 4], [1, 2, 3, 4]]
expected_result = "YES"

result = exchange(*test_case)

assert result == expected_result
```