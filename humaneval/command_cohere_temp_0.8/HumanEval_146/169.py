```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical `AND` operator (`&`) to intersect both odd first and last digits, reducing the necessity for multiple iterations. This approach eliminates unnecessary calculations and enhances performance, especially with larger arrays. 

To fully leverage the `&` operator, ensure the numerals are expressed as strings. Thus, the script omits odd-numbered digits when iterating through the array, guaranteeing only numbers with both odd first and last digits are counted.