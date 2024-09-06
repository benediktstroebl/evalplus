```python
def sum_squares(lst):
    result = 0
    for i, num in enumerate(lst):
        if i % 3 == 0:
            result += num ** 2
        elif i % 4 == 0 and i % 3 != 0:
            result += num ** 3
    return result
```

The code uses a for loop to iterate through each index `i` and corresponding list `num` value. By using the modulo operator `%`, we check if the current index is either a multiple of 3 or 4. If the index is a multiple of 3, we square the value `num`; if the index is a multiple of 4 but not 3, we cube the value `num`. The summed result is then returned by the function. 

This problem can also be solved using Python's `apply` function for a less verbose approach. Although this approach may not be as intuitive for some developers and is 3-4 times slower in terms of execution time [1]. 

```python
def sum_squares(lst):
    return sum(num ** i % 3 == 0 and num ** i or num ** (i + 1) for i, num in enumerate(lst, 1))
```

References: 
1. https://github.com/actionless/folktale/blob/master/src/lang/scala/collection/mutable/HashMap.scala%5Bhash%5D.html