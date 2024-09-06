```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nesting = 0
        idx = 0
        for char in chunk:
            if char == '(':
                nesting += 1
            else:
                nesting -= 1
            idx += 1
            if nesting < 0:
                break
        result.append(nesting)
    return result
```

This Python script can be translated directly into JS like this:
```javascript
function parseNestedParens(s) {
    var result = [];
    var nesting = 0;
    var idx = 0;
    for (var chunk of s.split(' ')) {
        for (var char of chunk) {
            if (char === '(') {
                nesting++;
            } else {
                nesting--;
            }
            idx++;
            if (nesting < 0) {
                break;
            }
        }
        result.push(nesting);
    }
    return result;
}
```

This JavaScript function operates similarly to the Python version. It iterates through each chunk of the input separated by spaces, maintaining nesting level `nesting` for each chunk. When encountering '(' it increases the nesting level and when encountering ')' it decreases it. The deepest nesting level reached within a chunk is pushed to the `result` array.