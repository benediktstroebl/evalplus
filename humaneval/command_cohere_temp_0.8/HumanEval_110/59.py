```python
def exchange(lst1, lst2):
    even_seen = False
    for elt in lst2:
        if not even_seen and elt % 2 == 0:
            even_seen = True
            continue
        if even_seen and elt % 2 != 0:
            return "NO"
    return "YES"
```

The script employs a straightforward `for` loop to iterate through the elements of `lst2`. It first verifies whether an even number has been encountered in `lst1`. If it has, the loop continues, ignoring the even numbers. It verifies whether the iterated element of `lst2` is odd and returns "NO" if it is, indicating that an even number from `lst1` couldn't be exchanged with an odd number from `lst2`. As there are no restrictions on the number of elements that may be exchanged, the algorithm only examines the odd numbers in `lst2` to find at least one even number to exchange with. It is worth noting that this approach assumes the input lists are of equal length or that the shorter one can be evenly partitioned between the two lists, as the algorithm does not take into account any potential truncation that could occur.