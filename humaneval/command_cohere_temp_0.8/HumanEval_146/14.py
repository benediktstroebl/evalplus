```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(x[0]) % 2 == 1]
    oddLast = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The script uses Python's ability to define a truthiness of the boolean values, such as the comparison of two sets returning true if the sets are equal means that the expression returns truthy data, otherwise, it returns a falsey data value. In this case, the `&` operator is used to "AND" the two sets together, and the length of the resulting set gives you the number of numbers that fulfill the required condition. Please ensure that you are using Python 3.7.0 or a later version because the behavior of the `&` operator with set values was introduced in this specific version of Python.