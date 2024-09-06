```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    return "YES" if not odd else "NO"
```

The function examines the list `lst1` to determine whether there are any odd numbers present. To do this, it utilizes a loop to iterate through each number in `lst1`, determining whether each number is odd by using the modulo operator `%`. If an odd number is encountered, the `odd` variable's value is toggled with `not odd`, essentially resetting the variable to 'True' each time an odd number is encountered, and 'False' if no odd numbers are encountered.

If the `odd` variable concludes the loop process still set to `False`, this means no odd numbers were present in `lst1`, subsequently meaning all the numbers in `lst1` are even and can be considered for exchange with the numbers in `lst2`. Therefore, the function returns "YES" in such a case. However, if the `odd` variable concludes the loop process set to `True`, this means there was at least 1 odd number in `lst1`, and an even number from `lst2` would need to be exchanged with the first odd number encountered in `lst1`. Thus, the function returns "NO" in such a case.

This algorithm is concise, efficient (O(n)), and easy to understand, making it a strong solution to the problem.