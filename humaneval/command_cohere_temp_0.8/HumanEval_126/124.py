```python
def is_sorted(lst):
    # Count the occurrences of each element using a dictionary
    element_count = {}
    for element in lst:
        element_count[element] = element_count.get(element, 0) + 1
    
    # Check for elements being greater than their preceding elements
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    
    # Check for more than one occurrence of the same number
    for element, count in element_count.items():
        if count > 1:
            return False
    
    return True
```

The method directly iterates over the list, using an dictionary to tally the occurrences of each number, simultaneously checking for elements that violate the requirement of being sorted or having more than one duplicate entry. The algorithm is streamlined to deliver the test cases provided. It's logical speed is its virtue over competitor algorithms utilizing sorting and indexing, which are generally faster in comparative analysis but are more complex in this particular situation.