```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = not odd
    if odd:
        return "NO"
    else:
        return "YES"
```
This Python script solves the problem with the `exchange()` function that takes two lists of numbers `lst1` and `lst2` as input and aims to determine if it's possible to exchange elements between them to make `lst1` a list of only even numbers. Here's how it works:
1. The function starts by initializing a boolean variable `odd` to `False`. This variable will be used to keep track of whether any odd numbers were encountered in `lst1`.
2. Next, the function iterates through each element in `lst1` using a `for` loop. For each element `x`, it checks if `x` is odd using the modulo operator (`%`). If an odd number is encountered, the `odd` variable is flipped (`not odd`) to indicate that an odd number was found.
3. After iterating through all the elements in `lst1`, the function checks the value of the `odd` variable. If `odd` is `False` (meaning no odd numbers were found in `lst1`), it means that it's possible to exchange elements with `lst2` to create a list of only even numbers. In this case, the function returns "YES".
4. If `odd` is `True`, it means at least one odd number was found in `lst1`, and therefore, it's not possible to create a list of only even numbers by exchanging elements with `lst2`. In this case, the function returns "NO".

This approach allows the function to efficiently solve the problem and provide the correct outcome ("YES" or "NO") based on the given lists.

I hope this helps, let me know if you have any further questions!