```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, checking if the index is odd and the element is even, then appends the element to `even_odd`. Finally, it returns the `even_odd` list, which signifies the odd indices holding even integers.

Here is a test drive code to test the function:
```python
test_list = [4, 2, 6, 7]
expected_result = [2]

actual_result = add(test_list)

print(actual_result)
```

The output will be:
```
[2]
``` 

This demonstrates that the function correctly identifies even elements at odd indices, as the `actual_result` aligns with the expected `expected_result`.  This problem can also be solved using the list comprehension in Python, here is an example:
```python
def add(lst):
    return [x for i, x in enumerate(lst) if i % 2 == 1 and x % 2 == 0]
```