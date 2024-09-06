```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            num = num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            num = num ** 3
        result += num
    return result
```

The function sums over the list `lst` and modifies each element `num` in the list according to the problem statement:
- If the index is a multiple of 3, the element is squared. 
- If the index is a multiple of 4 but not a multiple of 3, the element is cubed.

The sum is then returned as the output of the function.

This approach allows the function to solve the problem without changing the list itself, following the provided guidelines. 

*Note*: If feeling adventurous, there is an even more efficient solution possible with just one line: `sum(x**(2 if i%3 else 3) for i,x in enumerate(lst))`, but the given code is more readily understandable for folks starting out.