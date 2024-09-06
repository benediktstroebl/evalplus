Here is a self-contained Python script that solves the problem of separating nested parentheses:
```python
def separate_paren_groups(s):
    return ['(' + item + '') for item in s.json_parse(s, compact=False)]

def json_parse(s, compact=True):
    return json.loads(s)[1:] if compact else json.loads(s)
```

def json_encode(o):
    return json.dumps(o, sort_keys=True, indent=2)

def test_function():
    assert separate_paren_groups('( ) (( )) (( )( ))')') == ['()', '(())', '(()())']

def test_json_parse():
    assert json_parse('"foo"') == ['foo']

def test_json_encode():
    assert json_encode({'foo': 'bar'}) == '{"foo": "bar"}'

test_functions()
```
The `test_functions` function includes the test cases for `separate_paren_groups`, `json_parse`, and `json_encode` functions. The test cases ensure that the output of these functions aligns with the expected results.