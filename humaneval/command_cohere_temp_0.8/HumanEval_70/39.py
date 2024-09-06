```python
def strange_sort_list(lst):
    # Use dictionary to keep track of seen min and max values
    d = {}
    
    # Sorting and building result list at the same time
    result = []
    for v in lst:
        if v not in d:
            result.append(v)
        else:
            if len(d) == 1:
                result.append(d[-1])
            elif v > d[-2]:
                result.append(d[-1])
            else:
                result.append(d[-2])
            d[v] = v
    return result
```

The logic is straightforward:
1. We iterate over the input list.
2. For each element, we check if it's the smallest value seen so far (`not in d` checks if it's the first time we see this value). If so, we add it to our `result` list.
3. If it's not the first time we've seen this value (`v in d`), we check if there's only one value in our dictionary (`len(d) == 1`). If so, we've already seen the maximum value for this odd iteration step, so we add it to the result.
4. If there are multiple values in the dictionary (`len(d) != 1`), we compare the current value with the second-to-last value seen (i.e., the maximum value of the remaining integers, as per the weird sorting requirement). If the current value is greater, we add the last value seen to the result. Otherwise, we add the second-to-last value seen.
5. Finally, we add the current value to the dictionary to keep track of it for future comparisons.

This algorithm follows the "Strange Sorting" pattern, which helps to achieve the desired output.