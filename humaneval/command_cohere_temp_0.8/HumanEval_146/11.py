```python
def specialFilter(nums):
    oddFirsts = [x for x in nums if int(x[0]) % 2 == 1]
    oddLasts = [x for x in nums if int(x[-1]) % 2 == 1]
    return len(oddFirsts & oddLasts)
```

The script employs a logical operator (`&`) called "intersection" to combine two arrays (`oddFirsts` and `oddLasts`) and count the common elements that fulfill the given requirements. This leads to an efficient and concise solution.

To go further in depth on how the code works, when the function `specialFilter` is invoked with an array of numbers, it first uses a list comprehension to generate `oddFirsts`, which contains elements where the first digit is odd. Subsequently, it creates another list called `oddLasts`, comprising elements with odd last digits. Finally, the function employs the `len()` function to count the common elements in both `oddFirsts` and `oddLasts` and returns this quantity. 

This approach ensures that the function meets the problem requirements and results in an efficient and readable solution.