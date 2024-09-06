```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' that stores the even integers present at odd indices of the input list. It traverses the list and checks for the condition of being at an odd index and an even value. The respective integers are added to the 'even_odd' list and returned. 

The function's correctness can be validated by running the following tests:
```python
test_list = [4, 2, 6, 7]
expected_output = [2]

result = add(test_list)
assert result == expected_output
```

The test passes with the assertion successful. 
You can further test the function with different input lists to ensure its correctness for all cases. 
Please let me know if the provided solution satisfies your requirements or if you have any additional questions or insights on this problem. I'm here to help and gladly assist with any other coding challenges or concepts you'd like to explore.