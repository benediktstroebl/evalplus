```python
def add(lst):
    even_odd = []
    for i in range(len(lst)):
        if i % 2 == 1 and lst[i] % 2 == 0:
            even_odd.append(lst[i])
    return even_odd
```

This function defines an empty list 'even_odd' that stores the even integers present at odd indices of the input list. It traverses the list and verifies if the index is odd and the element is even, then it appends the element to the 'even_odd' list. Ultimately this function returns the 'even_odd' list. 

The following is a test suite that can be used to validate the functionality of this code:
```python
def test_add():
    # Positive test
    assert add([4, 2, 6, 7]) == [2]

    # Positive test
    assert add([1, 3, 5, 7, 2, 4]) == [2, 4]

    # Negative test, with all elements odd
    assert add([1, 3, 5, 7]) == []

    # Negative test, with no even integer at odd indices
    assert add([2, 4, 6, 8]) == []
```

Ensure that you incorporate this test suite into your codebase to scrutinize the function's correctness. 

This solution is concise and straightforward, offering a viable option to tackle the posed problem. It's important to keep your test suites comprehensive and varied to ensure maximum code coverage and security against potential glitches. 

Feel free to ask if you need further assistance or guidance on the best practices for coding problems, debugging strategies, or other Python-related queries.