```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function employs a simple logic to check for duplicates within the list. If there are any duplicates, it checks if there are any occurrences beyond the first one and returns False accordingly. If there are no duplicates, it returns True, indicating a sorted list. 

This problem can be solved in various ways, and the approach outlined above is just one possible solution. If you'd like to discuss alternative approaches or provide feedback, please let me know. 

This script can be tested against the examples provided in the problem statement as follows: 
```python
test_list = [5]
print(is_sorted(test_list))  # Should print True

test_list = [1, 2, 3, 4, 5]
print(is_sorted(test_list))  # Should print True

test_list = [1, 3, 2, 4, 5]
print(is_sorted(test_list))  # Should print False

test_list = [1, 2, 3, 4, 5, 6]
print(is_sorted(test_list))  # Should print True

test_list = [1, 2, 3, 4, 5, 6, 7]
print(is_sorted(test_list))  # Should print True

test_list = [1, 3, 2, 4, 5, 6, 7]
print(is_sorted(test_list))  # Should print False

test_list = [1, 2, 2, 3, 3, 4]
print(is_sorted(test_list))  # Should print True

test_list = [1, 2, 2, 2, 3, 4]
print(is_sorted(test_list))  # Should print False
``` 
This way, you can verify the function's correctness against the provided examples.