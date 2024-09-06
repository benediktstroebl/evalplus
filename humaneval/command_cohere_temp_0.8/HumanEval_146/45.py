```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script uses Python's array filtering functionality and the & operator for a shorter and more concise solution. The operator & returns the elements that are in both oddFirsts and oddLasts arrays. 

The function first creates two arrays, `oddFirsts` and `oddLasts`, using list comprehension, filtering the array of input `nums` to include only the elements where the first and respectively the last digit is odd. Then, using the & operator, it finds the common elements between `oddFirsts` and `oddLasts` arrays and returns their length with the `len()` function.