```python
def exchange(lst1, lst2):
    even_ Exchange lst1 for lst2 to get a list of only even numbers]]]);
    odd_  = [x for x in lst1 if x % 2 != 0]
    return "YES" if not odd_ else "NO"
```
The `exchange()` function evaluates to the following:
1. Destructive Exchange: To make the list of only even numbers, the odd numbers should be moved from `lst1` to `lst2`. This can be done by using another list comprehension `odd_ = [x for x in lst1 if x % 2 != 0]` to store all the odd numbers from `lst1`, and then `lst1` will become a list of even numbers.
2. Decision Making: Finally, the function returns `"YES"` if the list of odd numbers is empty (`not odd_`), meaning there are only even numbers in `lst1` after the destructive exchange. Otherwise, it returns `"NO"`. 

This approach ensures the original lists are not altered and operates on their copies. It also provides a more efficient solution, as the lists are processed sequentially, and the complexity is determined by the length of the input lists.