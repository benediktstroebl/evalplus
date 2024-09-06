```python
def smallest_change(arr):
    odd = sum(x%2 for x in arr)
    if odd % 2 == 0:
        return odd // 2
    else:
        return (odd + 1) // 2
```

The function works by counting the number of odd elements in the array. In a palindrome, every odd element is surrounded by another element or is at the beginning or end of the array. So, to make the array palindromic, we have to change every odd element to the another element or remove the odd element and add a new element to make it even, which makes the number of changes equal to the number of odd elements divided by 2. But if the number of odd elements is odd, we have to add one more change to make the last element even, hence `(odd + 1) // 2`. The rest of the logic remains the same.