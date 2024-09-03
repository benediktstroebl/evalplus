```python
def total_match(lst1, lst2):
    return lst1 if sum(1 for x in lst1 if x in lst2) > sum(1 for x in lst2 if x in lst1) else lst2

# Test cases
test = ['hi', 'admin']
test[['hI', 'Hi']]
test[['hi', 'project', 'admin', 'project'])
test[['4'])
test_negative = [['1', '2', '3', '4', '5'], ['4'])

# Test results
test.