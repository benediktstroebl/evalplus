```python
def triples_sum_to_zero(l: list):
    seen = set()
    for a in l:
        for b in l:
            if a != b and a + b in seen:
                return True
            seen.add(a)
    return False
```

This function employs a hashset 'seen' to keep track of elements encountered while looping through the list 'l'. For each element 'a', it iterates through the list and checks if there is another element 'b' that sums up to 'a' and hasn't been seen yet. If such a pair is found, the function returns 'True'. Otherwise, it returns 'False'. 

This approach has a time complexity of O(n^2) due to the nested loop structure, which makes it less efficient for large inputs.

This problem can be solved more efficiently using sorting and counting (with hash operations). Here's a revised solution:
```python
def triples_sum_to_zero(l: list):
    return any(x + y + z == 0 for x in l for y in l for z in l if x != y and x != z)
```

This approach creates three iterators 'x', 'y', and 'z' from the list 'l', and checks if the sum equals zero for any combination. This solution is more efficient with a time complexity of O(n^3), since it uses three levels of nested loops.  It is more optimized and suitable for larger datasets.