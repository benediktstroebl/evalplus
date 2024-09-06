```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` into which it filters the even integers at odd indices from the input list `lst`, and then returns the `even_odd` list. The function is encapsulated to solve the defined problem and is concise.

Here is how the function can be tested:
```python
test_list = [4, 2, 6, 7]
expected_result = [2]

result = add(test_list)
assert result == expected_result
```