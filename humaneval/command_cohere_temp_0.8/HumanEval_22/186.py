```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code explicitly iterates over each item in the input list `values`, and for each item, it checks if the item `isinstance(x, int)`; if that is the case, it includes the item in the resultant filtered list. 

This approach ensures that only integers are included in the output, as asked by the prompt, and the result is also a list, complying with the returned type. 

The markdown code block may be Directly copied and pasted into a Markdown document or README file to display the code and its description together, making it easier for developers to share their code and its functionality.