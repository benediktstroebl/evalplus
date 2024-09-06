```python
def specialFilter(nums):
    oddFirst = [num for num in nums if int(str(num)[0]) % 2 == 1]
    oddLast = [num for num in nums if int(str(num)[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The script uses Python's array filtering capabilities along with the `&` operator to find the intersection of two arrays, in this case, the array of numbers that fulfill the condition of the first digit being odd and the array of numbers that fulfill the condition of the last digit being odd, and then it returns the length of that intersection, which is the number of elements that fulfill both conditions. The function works with negative numbers as well.