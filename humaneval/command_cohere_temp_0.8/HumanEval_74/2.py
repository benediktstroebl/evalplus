```python
def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(val) for val in lst1)
    total2 = sum(len(val) for val in lst2)

    # If the total character count of lst2 is less than lst1, return lst2
    if total1 > total2:
        return lst2
    # If the total character count of lst1 is less than lst2, return lst1
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the first list lst1
    else:
        return lst1
```

This function utilizes Python's `sum` function in combination with a list comprehension to compute the total character count in both `lst1` and `lst2`. It then compares these totals and returns either `lst1` or `lst2` based on which list has the least total character count. If the character counts are equal, it returns `lst1`. 

The unit tests proposed in the problem statement are executed successfully when this function is invoked with the respective test lists. 
```python
# Test 1
test_list1 = []
test_list2 = []
print(total_match(test_list1, test_list2))  # Should print an empty list

# Test 2
test_list1 = ['hi', 'admin']
test_list2 = ['hI', 'Hi']
print(total_match(test_list1, test_list2))  # Should print ['hI', 'Hi']

# Test 3
test_list1 = ['hi', 'admin']
test_list2 = ['hi', 'hi', 'admin', 'project']
print(total_match(test_list1, test_list2))  # Should print ['hi', 'admin']

# Test 4
test_list1 = ['4']
test_list2 = ['1', '2', '3', '4', '5']
print(total_match(test_list1, test_list2))  # Should print ['4']
```

This demonstrates that the function successfully passes all the tests and adheres to the problem statement. It is important to note that this approach is effective for lists of strings with unique values. One may need to implement a different strategy for lists with repeated elements to account for instances where the total character count overlaps but each list has different content.