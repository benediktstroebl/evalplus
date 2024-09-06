```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above method creates two lists, `oddFirsts` and `oddLasts`, which contain all the numbers from `nums` that have odd first and last digits respectively. Then, it uses the `intersection` of these two lists to calculate the numbers that fulfill the requirements of having both odd first and last digits. Ultimately, it returns the length of this list, which represents the number of elements that satisfy the given criterion. 

This approach allows the function to efficiently solve the problem in a concise manner. 
The unit tests could be something like: 
 ```python
test = [(15, 1), (-73, 1), (14, 0), (-15, 0), (33, 2), (-2, 0), (-3, 0), (45, 1), (21, 0), (109, 1)]
for case in test:
    assert specialFilter(case[0]) == case[1]
```

This checks that the function behaves as expected for a variety of inputs.