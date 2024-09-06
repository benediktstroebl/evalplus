```python
def exchange(lst1, lst2):
    odd = lst1.count(2)
    even = lst2.count(2)
    if odd == 0 and even > 0:
        return "YES"
    elif even == 0 and odd > 0:
        return "NO"
    else:
        return "YES"
```

This Python script defines a function called `exchange` that takes two lists, `lst1` and `lst2`, as input. It aims to determine whether elements can be exchanged between these lists to make `lst1` contain only even numbers.

Here's how the function works:
1. It calculates the number of odd elements in `lst1` using the `count` method, which is denoted as `odd`.
2. Similarly, it calculates the number of even elements in `lst2` and assigns it to the variable `even`.
3. The function checks two conditions based on these counts:
   - If there are no odd elements in `lst1` (i.e., `odd` is 0) and there are more even elements in `lst2` than 0 (i.e., `even` is greater than 0), it means we can exchange elements to make `lst1` all even. In this case, it returns "YES".
   - If there are no even elements in `lst2` (i.e., `even` is 0) and there are more odd elements in `lst1` than 0 (i.e., `odd` is greater than 0), it means it is not possible to make `lst1` all even. In this case, it returns "NO".
4. If neither of the above conditions is met (which means there are odd elements in both lists), the function returns "YES" as it is still possible to exchange elements to achieve the goal.

The script assumes that the input lists will be non-empty, as stated in the problem statement. And the function returns "YES" or "NO" depending on the possibility of exchanging elements to make `lst1` contain only even numbers.