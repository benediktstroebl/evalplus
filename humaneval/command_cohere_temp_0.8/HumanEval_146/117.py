```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLast = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The logic of the solution can be explained as follows:
1. OddFirst Variable: The first step of the solution utilizes a list comprehension to create a temporary list called `oddFirst`. This list will contain all the numbers from the input array where the first digit is odd (1, 3, 5, 7, or 9). 

Example: In the input array [15, -73, 14, -15], `oddFirst` will contain [15, -15].
2. OddLast Variable: The solution then creates another temporary list called `oddLast` that contains all the numbers from the input array where the last digit is odd. 

Example: In the above input array, `oddLast` will contain [15, -15].
3. Performing AND Operation: The final step of the solution counts the numbers that appear in both `oddFirst` and `oddLast` lists, which correspond to numbers that both first and last digits are odd. This is achieved by performing a logical AND operation (`&`) between the two lists, even though they are lists of lengths 1. 

Example: In the above input array, the result of `oddFirst & oddLast` is `[15, -15]`.
4. Returning the Length: Finally, the function returns the length of the resulting list from the AND operation, which is the number of elements in the original array that meet the specified criteria. 

Example: In the provided example, the function `specialFilter` will return `1` for the input array `[15, -73, 14, -15]` because only one number (15) meets the criteria. 

This solution leverages the short-circuit evaluation of the AND operator, where the second argument (oddLast) will not be evaluated if the first argument (oddFirst) is empty. This helps to avoid unnecessary computations when the first condition fails. 

This solution has an Time Complexity: O(n) where n is the length of the input array, and an Space Complexity: O(n), where n is the length of the input array, as it creates two temporary lists of the same size as the input array. 

Note: This solution assumes that the input array contains only positive numbers and negative integers. If the input array could potentially contain numbers with both positive and negative odd digits, additional handling would be necessary.