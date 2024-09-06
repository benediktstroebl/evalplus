```python
def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = len(lst1)
    
    if even_occurrences == total_occurrences:
        return "YES"
    elif even_occurrences > total_occurrences:
        # More even numbers than odd in lst1, so we can take from lst2
        return "NO"
    else:
        # Odd numbers are more, so we can give to lst2 without any odd numbers left in lst1
        return "YES"
```

The function first counts the occurrences of even numbers in `lst1`, and uses the `len()` function to get the total number of elements in `lst1`.

If there are the same number of even and odd numbers, we are done, as `lst1` will already be all even numbers.

If there are more even numbers than odd in `lst1`, we cannot turn it into a list of all even numbers, so we return "NO".

If there are more odd numbers than even in `lst1`, we can give all the odd numbers to `lst2`, and still have a list of all even numbers in `lst1`. 

This assumes that the lists are non-empty, as stated in the problem statement. Let me know if you'd like anything explained differently!