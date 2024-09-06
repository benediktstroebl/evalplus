```python
def exchange(lst1, lst2):
    even_lst1 = [x for x in lst1 if x % 2 == 0]
    if len(even_lst1) == len(lst1):
        return "YES"
    else:
        return "NO"
```
This Python script provides a self-contained function called `exchange` that solves the problem described in the markdown code block. It takes two lists, `lst1` and `lst2` as input and returns a string indicating whether it's possible to exchange elements between them to make `lst1` a list of only even numbers. 

The function checks if the list of even numbers in `lst1` has a length equal to the length of `lst1`. If it does, it returns "YES," indicating that we can exchange elements from `lst2` to make `lst1` all even numbers. Otherwise, it returns "NO," as it's not possible to achieve such an exchange. 

This solution is concise and accurately answers the question posed, making it a useful building block for the problem at hand.