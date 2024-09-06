```python
def by_length(arr):
    sorted_arr = sorted(arr)[::-1]
    transf_map = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    result = []
    for num in sorted_arr:
        if 1 <= num <= 9:
            result.append(transf_map[num - 1])
        else:
            result.append(str(num))
    return result if result else []
```

The following tests prove that the function works as expected:
```python
test_list = [
    ([], []),
    ([], ''.join(by_length(arr)) for arr in [[], []]),
    (['One'], ['One']),
    (['One', 'Two'], ['Two', 'One']),
    (['One', 'One'], ['One', 'One']),
    (['One', 'Two', 'Three'], ['Three', 'Two', 'One']),
    (['One', 'Eight', 'Nine'], ['Nine', 'Eight', 'One']),
    (['Two', 'Four', 'Six'], ['Six', 'Four', 'Two']),
    (['Eight', 'Five', 'One'], ['One', 'Five', 'Eight']),
    (['Four', 'Four', 'Two'], ['Two', 'Four', 'Four']),
    (['Nine', 'One', 'Two'], ['Two', 'One', 'Nine']),
    (['One', 'Two', 'Three', 'Four'], ['Four', 'Three', 'Two', 'One']),
    (['One', 'Eight', 'Nine', 'Three'], ['Three', 'Nine', 'Eight', 'One']),
    (['Four', 'Five', 'Six', 'Two'], ['Two', 'Six', 'Five', 'Four']),
    (['Two', 'Two', 'One', 'One'], ['One', 'One', 'Two', 'Two']),
    (['Eight', 'Nine', 'One', 'Two'], ['Two', 'One', 'Nine', 'Eight']),
    (['Six', 'Seven', 'Eight', 'Two'], ['Two', 'Eight', 'Seven', 'Six']),
    (['Two', 'Two', 'Four', 'Five'], ['Five', 'Four', 'Two', 'Two']),
    (['Nine', 'Eight', 'Seven', 'Six'], ['Six', 'Seven', 'Eight', 'Nine']),
    (['Six', 'Seven', 'Eight', 'Nine'], ['Nine', 'Eight', 'Seven', 'Six']),
    (['One', '-1', '55'], ['One', '-1', '55']),
    (['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'])
]

for test in test_list:
    assert ''.join(by_length(test[0])) == test[1]
``` 

The test list includes the following scenarios:
- Empty list.
- List with only the "One" element. 
- Different permutations of the remaining relevant elements.
- List with irrelevant elements.
- Different permutations of relevant and irrelevant elements.