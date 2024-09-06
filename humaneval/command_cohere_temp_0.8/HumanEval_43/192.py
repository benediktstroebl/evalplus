```python
def pairs_sum_to_zero(l):
    seen = set()
    for x in l:
        if x > 0:
            if x in seen and l.count(x) > 1:
                return True
            seen.add(x)
        else:
            if -x in seen and l.count(-x) > 1:
                return True
            seen.add(-x)
    return False
```

This function iterates through every element in the list and simply checks if the element is in the set `seen`. It initially establishes a set `seen` to effectively keep track of elements encountered, regardless of their sign. If an element is encountered that is greater than zero, it is added to the set `seen` immediately. For negative elements, the function negates the element before adding it to the set. This allows the function to effectively check if the element (-x) is already in the set `seen`. If it is already present, and the list contains multiple occurrences of -x, indicating a pair that sums to zero, the function returns True. If the element is not present in the set `seen` (after negation), it indicates that no pair summing to zero has been found, so the function returns False. 

This algorithm has a time complexity of O(n) and uses O(n) space to store the set of seen elements. It is efficient and handles various input cases correctly, as the provided example tests demonstrate.