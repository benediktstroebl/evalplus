```python
def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    return min(odd, len(arr) - odd)
```

The function works by counting the number of odd elements in the array (`odd`) and comparing it to the number of even elements in the array (`len(arr) - odd`) as a palindrome can be achieved by flipping the odd elements and/or flipping the even elements. The minimum of these two counts represents the minimum number of changes required to form a palindrome.