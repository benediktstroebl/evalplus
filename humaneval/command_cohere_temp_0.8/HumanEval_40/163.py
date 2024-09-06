```python
def triples_sum_to_zero(lst):
    # Use Counter to count occurrences of elements in the list
    cnt = Counter(lst)
    
    # Check if any two elements have a sum of the third distinct element
    for el1, el2 in cnt.items():
        if el1 + el2 == 0 and len(cnt) == 2:
            return True
    
    return False
```

This approach utilizes Python's `Counter` from the `collections` module to efficiently count the occurrences of each element in the list. Then, it checks if any pair of elements have a sum equal to the third distinct element in the list. If such a pair is found, the function returns `True`; otherwise, it returns `False`. 

This code block is optimized for efficiency and is less prone to time complexity issues compared to iterative brute-force approaches.