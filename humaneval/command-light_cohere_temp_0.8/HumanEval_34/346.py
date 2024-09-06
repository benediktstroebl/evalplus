```python
def unique(lst):
    seen = set()
    result = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            result.append(x unique(seen))
    return result

# Test cases
test_unique_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
test_empty = []
test_single = [5]
test_duplicates = [3, 3]

# Function call
result = unique(test_unique_list)
print("Unique list:", result)

result = unique(test_empty)
print("Unique list:", result)

result = unique(test_single)
print("Unique list:", result)

result = unique(test_duplicates)
print("Unique list:", result)
```
This Python script presents a function named **`unique`** that processes a list of elements and seeks to deliver a list of their distinct elements. The function creates a set of unique elements and subsequently constructs a new list with these unique values, ensuring that the output list is free of duplicates.

The script also includes a collection of test cases, comprising various scenarios, to verify the accuracy of the function. When the **`unique`** function is called with these test cases, the output displays the distinct elements derived from each list.