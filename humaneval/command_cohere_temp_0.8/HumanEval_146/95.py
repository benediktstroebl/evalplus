```python
def specialFilter(nums):
    oddFirst = lambda x: x[0] % 2 == 1 and x[1] % 2 == 1
    oddLast = lambda x: x[-1] % 2 == 1 and x[-2] % 2 == 1
    return sum(n for n in nums if oddFirst(n) and oddLast(n) and n > 10)
```

The solution filters numbers greater than 10 that have odd first and last digits and then counts the number of elements that satisfy this condition using the `sum()` function. 

To achieve this, two lambda functions, `oddFirst` and `oddLast`, are used to respectively filter elements where the first and last digits are odd. 

The lambda functions are reusable filters that can be used in chains to achieve the desired filtering outcome. 

The solution is self-contained and does not rely on any external modules other than the Python standard library. 

To test this function, you can call it with a list of strings and verify that the number of elements that satisfy the specified conditions is correctly counted.