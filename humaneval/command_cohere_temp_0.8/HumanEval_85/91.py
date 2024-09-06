```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list `lst`. It iterates through the list, checking if the index is even and the element is also even. If so, it appends the element to `even_odd`. Finally, the function returns the `even_odd` list. 

To ensure this script correctly solves the problem, test the function with the following input:
```python
test_list = [4, 2, 6, 7]
expected_result = [2]

assert add(test_list) == expected_result
```

The expected outcome for the function is a list consisting of only the even elements found at odd positions in the input list.