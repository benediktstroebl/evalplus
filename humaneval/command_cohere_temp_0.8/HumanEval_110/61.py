```python
def exchange(lst1, lst2):
    odd = False
    for x in lst1:
        if x % 2:
            odd = True
            break
    
    if not odd:
        return "YES"
    
    res = lst1[:]
    for x in lst2:
        if x % 2:
            res.append(x)
    return "NO"
```

The function `exchange` takes two lists, `lst1` and `lst2`, and returns "YES" if it's possible to exchange elements between them to make `lst1` a list of only even numbers. If it's not possible, it returns "NO". The function first checks if the current `lst1` has an odd number. If not, it returns "YES" since `lst1` already has only even numbers. If there is an odd number in `lst1`, the function adds all the even numbers from `lst2` to the `res` list that initially is a copy of `lst1`. Then the function returns "NO" because the `res` list has only even numbers, and the odd number from `lst1` was moved to `lst2`. 

Here is a basic understanding of lists and basic loops like `for` and `if` which can be helpful when trying to solve this problem and understand the code above. Lists are mutable arrays that are defined by enclosing the elements between square brackets `[]` and can be of any data type. The `for` loop is used to iterate over each element in a list and can be written with or without an `Iterator` (the variable that represents each element in the list). The `if` statement can be used to selectively execute code based on the truthiness of a condition, returning a value or taking action.