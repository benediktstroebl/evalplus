```python
def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(el) for el in lst1)
    total2 = sum(len(el) for el in lst2)

    # If the total character count of lst2 is less than lst1, return lst2
    if total1 > total2:
        return lst2
    # If the total character count of lst1 is less than lst2, return lst1
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the lexicographically smaller list
    else:
        return min(lst1, lst2)
```

This function compares the total number of characters in both lists and returns the list with fewer total characters. If both lists have the same number of characters, it returns the lexicographically smaller list. The function is designed to handle various scenarios, including cases where the lists have different lengths and cases where the lists have the same number of characters. 

Here is a simple unit test for this function:
```python
def test_total_match():
    # Test 1
    input1 = ['hi', 'admin']
    input2 = ['hI', 'Hi']
    expected = ['hI', 'Hi']
    assert total_match(input1, input2) == expected

    # Test 2
    input1 = ['hi', 'admin']
    input2 = ['hi', 'hi', 'admin', 'project']
    expected = ['hi', 'admin']
    assert total_match(input1, input2) == expected

    # Test 3
    input1 = ['4']
    input2 = ['1', '2', '3', '4', '5']
    expected = ['4']
    assert total_match(input1, input2) == expected

    # Test 4
    input1 = ['hi', 'admin']
    input2 = ['hI', 'hi', 'hi']
    expected = ['hI', 'hi', 'hi']
    assert total_match(input1, input2) == expected

test_total_match()
``` 
This will produce the following output:
```bash
>>> test_total_match()
``` 

This simple test suite verifies the basic functionality of the `total_match` function against its intended behavior as described in the prompt. 

The test suite can be expanded to cover a wider range of scenarios, including different list lengths, character distributions, and combinations of strings.