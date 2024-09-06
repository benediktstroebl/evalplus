```python
def sort_third(l: list):
    """Sorts a list of integers so that values divisible by three appear first.

    : We uses the0.
    for i in range(len(l)):
        if l[i] % 3 == 0:
            l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
    return l

#Test cases
print(sort_third([1, 2, 3]))    #Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  #Expected output: [2, 6, 3, 4, 8, 9, 5]
```