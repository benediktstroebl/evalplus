```python
def smallest_change(arr):
    odd, even = 0, 0
    for n in arr:
        if n == n[::-1]:
            even += 1
        else:
            odd += 1
    if odd % 2 == 0:
        return odd // 2
    else:
        return even
```

The function `smallest_change` calculates the minimum number of changes to make the array palindromic based on the difference between the counts of odd and even elements in the array, leveraging the fact that the number of changes required to make an odd-length palindrome is always twice the number of changes for an even-length palindrome. The code is concise and efficient, solving the problem in a straightforward manner.