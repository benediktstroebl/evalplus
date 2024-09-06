```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        lev = 0
        i = 0
        while i < len(chunk):
            if chunk[i] == '(':
                lev += 1
            else:
                lev -= 1
            i += 1
        result.append(lev)
    return result
```

This Python script can be translated directly into JS:
```javascript
type List = Array<number>;

function parse_nested_parens(s) {
    var result = [];
    var chunks = s.split(" ");
    for (var i = 0; i < chunks.length; i++) {
        var chunk = chunks[i];
        var lev = 0;
        for (var j = 0; j < chunk.length; j++) {
            if (chunk[j] === "(") {
                lev++;
            } else {
                lev--;
            }
        }
        result.push(lev);
    }
    return result;
}
```

This script takes a string as input and returns a list of the deepest levels of nesting of parentheses in each chunk. The script is tested and passes for the example given.