```python
def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(int(d) % 2 for d in digits)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r
```

The code leverages Python's string formatting along with a generator expression for efficient odd digit counting. This produces the desired output without any unnecessary list conversions, resulting in a concise and effective solution. Test cases can be run to verify the accuracy of the provided solution.