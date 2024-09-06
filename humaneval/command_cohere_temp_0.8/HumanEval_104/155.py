```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c not in '02468')) for i in x if int(''.join(c for c in str(i) if c not in '02468')) == i]
    return sorted(odd)
```

The algorithm for this solution is fairly straightforward. It converts each integer to a string, removes all even digits, converts them back to integers, and then filters out the ones that aren't equal to themselves after removing even digits. Finally, it sorts the resulting list in ascending order as mandated by the spec. 

This solution utilizes a common Pythonic technique of manipulating data as strings before converting it back to numbers for numerical operations. By converting the integers to strings, we can take advantage of Python's powerful string manipulation capabilities.