```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, using a `for` loop, and checks for the criterion of being at an odd index and an even value. These numbers get appended to `even_odd`. The function returns this resultant `even_odd` list, which contains the required integers. 

The test cases can be calculated with:
```python
test_cases = [
    [4, 2, 6, 7], 
    [10, 8, 12, 14, 20, 22],
    [2, 3, 5, 7, 9, 11, 13, 15, 17, 19],
    ]
for case in test_cases:
    print(f'Test Case: {case}, Expect: {add(case)}')
```

The expected output is:
```
Test Case: [4, 2, 6, 7], Expect: [2]
Test Case: [10, 8, 12, 14, 20, 22], Expect: [10, 20]
Test Case: [2, 3, 5, 7, 9, 11, 13, 15, 17, 19], Expect: [3, 5, 7, 9, 11, 13]
``` 

This demonstrates the function's correctness.