```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list `even_odd` that stores the even integers positioned at odd indices from the input list. It achieves this by iterating through each index in the input list, using the modulus operator to check if the index and the value at that index are both even. If they are, it appends the value to the `even_odd` list.

The result is a list of even integers located at odd indices in the original list. 

If you'd like, I can provide more explanations or example tests to ensure the script is well-understood and airtight.