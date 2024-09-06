```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, checking if the index is odd and the element is even, then appends the element to `even_odd`. Finally, the function returns the `even_odd` list, which stores the required even elements. 

Here is a test drive code to test the function:
```python
test_list = [4, 2, 6, 7]
expected_result = [2]

actual_result = add(test_list)

print(actual_result)
```
The output will be:
```python
[2]
``` 

This confirms that the function adheres to the problem statement and successfully isolates the even integers found at odd indices in the list.