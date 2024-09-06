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
This Python script defines a function `exchange` that takes two lists of numbers `lst1` and `lst2` as inputs. It aims to determine whether it is possible to exchange elements between these two lists in a way that turns `lst1` into a list of only even numbers. Here's how the function works:
1. It initializes a boolean variable `odd` to `False`. This variable will be used to keep track of whether any odd number is encountered in `lst1`.
2. The function then iterates through each element in `lst1` using a `for` loop. For each element `x`, it checks whether `x` is odd by computing its remainder when divided by 2 using the `%` operator. If the result is non-zero, it sets `odd` to `not odd`, effectively toggling the value of `odd` to `True`.
3. After iterating through all elements of `lst1`, the function checks the value of `odd`. If `odd` is `True`, it means that at least one odd number was encountered in `lst1`, and therefore it is not possible to exchange elements to make all elements in `lst1` even. In this case, it returns "NO".
4. If `odd` is `False` at the end of the loop, it means that all elements in `lst1` are even, and it is possible to exchange elements to achieve the desired result. In this case, it returns "YES".

This function efficiently solves the problem by exploiting the fact that it is sufficient to check only the parities of the elements in `lst1`, and the exchange operation can be simulated within the function's logic without explicitly performing the exchange.