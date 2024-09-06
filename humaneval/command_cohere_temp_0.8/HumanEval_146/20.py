```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The above code uses Python's list comprehension to filter elements that have odd first digits and odd last digits, and finally finds the intersection of these two lists using the & operator to get the shared elements. 

The markdown code block for the solution will look as follows:
```python
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
```