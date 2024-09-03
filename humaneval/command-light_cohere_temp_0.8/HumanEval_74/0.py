Here's a Python script that contains a self-contained function that solves the problem you described:
```python
def total_match(lst1, lst2):
    # The lists must have the same length
    if len(lst1) != len(lst2):
        return []
    
    # Initialize a new list to store the result
    result = []
    
    # Loop through the lists and compare characters
    for i in range(len(lst1)):
        if lst1[i] < lst2[i]:
            result.append(lst1[i])
        else:
            result.append(lst2[i])
    
    return result

# Test cases
test_cases = [
    [], ['hi']
    ['4'], ['1', '2', '3', '4', '5']
    ['hi', 'admin'], ['hI', 'Hi']
]

# Function call
for test in test_cases:
    print(total_match(test, ['hi', 'admin']))
```
The function total_match takes two lists of strings as input and returns a new list containing the strings from the list with the least number of characters. The first list must have a character less than the second list's character, or vice versa.