```python
def flip_case(string: str) -> str:
    return ''.joincase(string)

#Test case 1
assertEqual('Hello', flip_case('Hello'))
#Test case 2
assertEqual('world', flip_case('World'))
#Test case 3
assertNotEqual('HOUSE', flip_case('House'))
#Test case 4
assertNotEqual('heLLo', flip_case('Heello'))
```
I hope this passes all the test cases.  Let me know if there's anything else I can assist you with.