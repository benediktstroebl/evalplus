```python
def exchange(lst1, lst2):
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_ev = sum(x % 2 == 0 for x in lst2) - even_found
    return "YES" if count_diff_ev >= 0 else "NO"
```

The function `exchange()` takes two lists, `lst1` and `lst2`, as its input and returns a string indicating whether it is possible to exchange elements between them to make lst1 a list of only even numbers. To make the decision, the function uses the `any()` and `map()` functions to check if lst1 has at least one even number. Then it counts the number of even numbers in `lst2`, and subtracts the result from the count of even numbers in `lst1`. If the result is greater than or equal to 0, this means we can give from `lst2` to `lst1` enough even numbers to make `lst1` all even, so the function returns `"YES"`. Otherwise, it returns `"NO"`. 

The code assumes that the input lists will be non-empty, as stated in the problem statement. And even though these assumptions are mentioned in the statement, it is always good to make sure the input is valid before making conclusions. The following code extends the above code to also validate the input: 

```python
def exchange(lst1, lst2):
    assert len(lst1) > 0, "Input list lst1 is empty."
    assert len(lst2) > 0, "Input list lst2 is empty."
    even_found = any(map(lambda x: x % 2 == 0, lst1))
    count_diff_ev = sum(x % 2 == 0 for x in lst2) - even_found
    return "YES" if count_diff_ev >= 0 else "NO"
```

The code above uses the `assert` statement to check for any of the input lists being empty. If any of the lists is empty, the `assert` statement will cause the program to stop and produce an error message referencing the assertion that failed, which will be one of the two `assert` statements in the code.  This way, the program makes sure that the input is checked, and prevents any out-of-bounds access in case of empty lists.