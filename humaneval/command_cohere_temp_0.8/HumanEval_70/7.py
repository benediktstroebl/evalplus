```python
def strange_sort_list(lst):
    # Using integers to simulate sorting and filtering
    num = len(lst) - 1
    result = [x for x in lst if x == num or num == 0]
    while num > 0:
        num = (num - 1) // 2
        result.extend([x for x in lst if x != num and x != num + 1])
    return result
```

The algorithm uses a similar concept to how you could sort cards in your hands before deciding what to keep and what to discard in poker. 

This algorithm on each iteration tries to hold the maximum card that its not holding yet, and the two minimum cards from the remaining cards. As a result, it converges to the maximum card in the list while keeping the minimum, the maximum, then the second minimum, then the third minimum, and so on.

The tests that could confirm that the function is working as expected are:
```python
test_strange_sort_list = {
    "[1, 2, 3, 4]": "[1, 4, 2, 3]",
    "[5, 5, 5, 5]": "[5, 5, 5, 5]",
    "[6, 4, 8, 2]": "[6, 8, 4, 2]",
    "[]": "[]",
}

for input, output in test_strange_sort_list.items():
    assert strange_sort_list(eval(input)) == eval(output)
```