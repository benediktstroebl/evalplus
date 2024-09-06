```python
def smallest_change(arr):
    ans = float('inf')
    for a in set(arr):
        tem = arr.count(a)
        if tem % 2 == 0:
            continue
        count = 0
        for b in arr:
            if b == a:
                count += 1
        ans = min(ans, count)
    return ans
```

The function `smallest_change()` iterates through the unique elements in the array, and for each unique element `a`, it calculates the count of occurrences of `a` in the array. If this count is even, it means that changing all occurrences of `a` to another value won't make the array palindromic, so it continues to the next iteration. If the count is odd, the function calculates the minimum number of changes required to change all occurrences of `a` to another value, and updates the answer if the current count is smaller. Finally, the function returns the minimized number of changes needed to make the array palindromic. 

Here is a simpler approach that solves the problem:
```python
def smallest_change(arr):
    odd = []
    even = []
    for n in arr:
        if arr.count(n) % 2:
            odd.append(n)
        else:
            even.append(n)
    return min(len(odd), len(even))
```

This solution categorizes the numbers in the array into odd and even occurring numbers. The smallest number of changes required to make the array palindromic for each category is the lesser of the length of odd and even occurring numbers.