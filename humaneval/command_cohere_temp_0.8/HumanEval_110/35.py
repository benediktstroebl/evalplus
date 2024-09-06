```python
def exchange(lst1, lst2):
    even_occurrences = sum(x % 2 == 0 for x in lst1)
    total_occurrences = sum(x % 2 == 0 for x in lst1)
    if even_occurrences == total_occurrences:
        return "YES"
    return "NO"
```

The method directly determines the number of occurrences of even numbers in `lst1` using the `sum` function in combination with a generator expression. After that, it calculates the total number of even numbers in both lists using the same approach and checks if the two values are equal. If they are, it returns "YES" since an even number can be moved from `lst2` to `lst1` to make the target list consist of even numbers only. If the counts aren't the same, it returns "NO," as no such exchange of elements would work. 
This solution has a time complexity of O(n) and a space complexity of O(1), which makes it an efficient solution for this problem.