```python
def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    even_lst2 = [x for x in lst2 if x % 2 == 0]
    if len(even_lst1) == len(lst1) and len(even_lst2) == len(lst2):
        return "YES"
    return "NO"
```

The function first uses list comprehension to filter even numbers from both `lst1` and `lst2`. The script checks whether the lengths of these filtered lists are equal to the original lists' lengths, using the condition `len(even_lst1) == len(lst1)` and `len(even_lst2) == len(lst2)`. If this condition is true, return `"YES"`, else return `"NO"`.

This approach takes advantage of the problem's assumption that the input lists will only contain even numbers or odd numbers, and thus a combination of these lists can only result in an evenly sized list of even numbers if it's possible to produce `lst1` from `lst2` by exchanging elements.

This solution adheres to the problem's specification that states there's no limit on the number of exchanged elements between `lst1` and `lst2`. 

The code is designed to be self-contained and not rely on any external variables or functions, making it easy to understand and directly applicable.  It also follows the given Python style and formatting guidelines, making it easy to understand and adopt by the user.  Test cases are also not included in the code, as per the user's request.  However, it is recommended to include them for robustness and reliability of the code.  Overall, the code provides an efficient solution to the problem with a clear and understandable code style.  The user can freely adopt this code for their specific needs.