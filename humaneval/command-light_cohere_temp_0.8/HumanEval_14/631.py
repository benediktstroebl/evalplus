```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # tests
 using assert to ensure validity of the output
    assert len(all_prefixes('abc')) == 3
    assert all_prefixes('abcd') == ['ab', 'bc', 'cd']
    assert all_prefixes('') == []
    assert all_prefixes('___oo_') == []
``` 
This version ensures the validity of the output by using assert statements to check the output against expected values.