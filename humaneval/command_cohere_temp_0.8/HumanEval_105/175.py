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

The following tests will confirm that the function behaves as expected:
```python
test_list = [
    ([], []),
    ([], ''.join),
    (['One'], 'One'),
    (['One', 'Two'], 'One', 'Two'),
    (['One', 'Two', 'Three'], 'One', 'Two', 'Three'),

    (['One', 'One', 'Two', 'Two'], 'One', 'One', 'Two', 'Two'),
    (['One', 'One', 'Two', 'Three', 'Four'], 'One', 'One', 'Two', 'Three', 'Four'),
    (['One', 'One', 'Two', 'Three', 'Four', 'Five'], 'One', 'One', 'Two', 'Three', 'Four', 'Five'),

    (['One', 'Two', 'Three', 'Four', 'Five', 'Six'], 'One', 'Two', 'Three', 'Four', 'Five', 'Six'),
    (
        ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven'],
        'One',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
    ),

    (['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight'],
         'One',
         'Two',
         'Three',
         'Four',
         'Five',
         'Six',
         'Seven',
         'Eight'),

    (['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'],
     'One',
     'Two',
     'Three',
     'Four',
     'Five',
     'Six',
     'Seven',
     'Eight',
     'Nine'),

    (['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'],
     'One',
     'Two',
     'Three',
     'Four',
     'Five',
     'Six',
     'Seven',
     'Eight',
     'Nine'),

    (['Eleven', 'Twelve', ' Thirteen'], 'Eleven', 'Twelve', 'Thirteen'),
    (['Eleven', 'Twelve', ' Thirteen', 'Fourteen'], 'Eleven', 'Twelve', 'Thirteen', 'Fourteen'),
    ([' Fifteen', ' Sixteen'], ' Fifteen', ' Sixteen'),

    (['One', 2, 'Three', 4, 5, 6, 'Eight'], 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Eight'),
    (['One', 2, 'Three', 4, 5, 6, 'Eight', 'Nine'], 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Eight', 'Nine']),
    (['One', 2, 'Three', 4, 5, 6, 'Eight', 'Nine', 10],
     'One',
     'Two',
     'Three',
     'Four',
     'Five',
     '