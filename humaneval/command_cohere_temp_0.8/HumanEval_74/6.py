```python
def total_match(lst1, lst2):
    l1_total = sum(len(x) for x in lst1)
    l2_total = sum(len(x) for x in lst2)
    
    if l1_total < l2_total:
        return lst1
    elif l2_total < l1_total:
        return lst2
    else:
        return [x for x in lst1 if x not in lst2]
```

The problem boils down to comparing the total character count of all strings in both lists. If one list has a smaller total character count, it will remain unchanged. The second list will have strings removed if they are present in the first list and have a larger character count. The resulting list is then returned. 

The unit tests are embedded within the code block for ease of use. They include test cases that cover edge scenarios like empty lists, lists with different lengths, and lists of different content. 
```python
test_lists = [([], []),
               =['hi', 'admin', 'project', 'hub'], ['hI', 'Hi', 'admin', 'project', 'hub'],
                ['hi', 'admin'], ['hI', 'Hi', 'admin'], 
                ['hI', 'Hi', 'admin', 'project'], ['hi', 'admin', 'project'], 
                ['1', '2', '3', '4', '5'], ['1', '2', '3', '4'], 
                ['4'], ['1', '2', '3', '4', '5'],
                ['hi', 'admin', 'hub'], ['hI', 'Hi', 'admin', 'project', 'hub']]

for l1, l2 in test_lists:
    assert total_match(l1, l2) == expected_result
```

The `total_match` function can be applied to solve problems involving string similarity or list comparison, such as finding duplicates or keeping only the most informative strings from a list.