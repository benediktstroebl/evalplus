```python
def will_it_fly(q, w):
    return (sum(q) <= w) and (w == q[0] + q[-1] == sum(q[1:-1]) or w == sum(q))
```

The function checks if the list is palindromic by comparing the first and last elements of the list, if they are the same, it then compares the sum of the middle elements to the total weight and whether or not the list is empty. 

The total weight can be exceeded in two cases:
1. If the list is empty.
2. If the first and last elements are the same, and the list is not empty. 

So we have the conditions `q[0] == q[-1]` and `q.index(q[0]) != len(q) - 1` to cover the two cases for checking a palindromic list. 

I hope this helps! Let me know if you would like me to explain any part of the code in detail.