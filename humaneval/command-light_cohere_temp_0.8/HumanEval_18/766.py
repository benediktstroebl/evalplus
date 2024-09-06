```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join
    sub = substring
    
    while sub in string:
        count += 1
        string += sub
    return count

# Test cases
test_1 = [('a', 'a')]
test_2 = [('aaa', 'aa')]
test_3 = [('aaaa', 'aa')]

test_res = []
for test in test_1:
    test_res.append(how_many_times(*test))
print(test_res)

test_res = []
for test in test_2:
    test_res.append(how_many_times(*test))
print(test_res)

test_res = []
for test in test_3:
    test_res.append(how_many_times(*test))
print(test_res)
 ```