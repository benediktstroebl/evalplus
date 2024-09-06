```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It traverses the list, checking if the index is odd and the element is even, then appends the element to `even_odd`. Finally, the function returns the `even_odd` list, resulting in the needed odd-positioned even integers. 

The function adheres to the provided problem statement and expects a list input. It returns a list of integers as expected by the problem statement. While the function works for the provided example in the comment, it's worth noting that the first element of the list (index 0) is a correct Odd-indexed, Even integer (4), hence the function only returns the 2nd element (index 1), which is [2]. 

The function assumes the list is non-empty; if the list could be empty, the function should be modified to handle this scenario.