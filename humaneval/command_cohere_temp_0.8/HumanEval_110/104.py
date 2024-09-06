```python
def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = sum(x % 2 == 0 for x in lst1)+sum(x % 2 == 0 for x in lst2)
    if even_occurrences == total_occurrences:
        return "YES"
    return "NO"
```

The function uses a simple algorithm that checks the occurrence of even numbers in the first list `lst1` and the total occurrence of even numbers in both lists. If the occurrence of even numbers in the first list is equal to the total occurrence of even numbers in both lists, it is possible to exchange elements to make the list of only even numbers, and the function returns "YES". Otherwise, it returns "NO". 

The function assumes no constraints on the input lists' length and the values in them. You can test the function by calling it with different input lists and verifying the output against the problem statement. 

Let's prove the correctness of the approach by taking one element from `lst2` and append it to `lst1`. Suppose after the first exchange, the following states are true:
1. The total number of even elements in both lists is still the same.
2. The number of even elements in the list `lst1` has increased by 1.

Because of the symmetry of the approach and the element exchange, we can continue to exchange elements from `lst2` to `lst1` until the first list contains only even numbers. 

Thus, the approach is correct, and the function solves the problem as stated.  If it is possible to exchange elements between the lst1 and lst2 to make all the elements of lst1 to be even, return "YES". Otherwise, return "NO".